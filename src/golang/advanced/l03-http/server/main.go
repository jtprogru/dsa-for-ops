// Демо HTTP-сервера: Go 1.22+ routing, middleware, graceful shutdown.
package main

import (
	"context"
	"encoding/json"
	"log"
	"net/http"
	"os/signal"
	"syscall"
	"time"
)

type User struct {
	ID   string `json:"id"`
	Name string `json:"name"`
}

func handleUser(w http.ResponseWriter, r *http.Request) {
	id := r.PathValue("id")
	u := User{ID: id, Name: "Пользователь " + id}
	w.Header().Set("Content-Type", "application/json")
	_ = json.NewEncoder(w).Encode(u)
}

func handleHealth(w http.ResponseWriter, r *http.Request) {
	_, _ = w.Write([]byte("ok"))
}

func loggingMiddleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		start := time.Now()
		next.ServeHTTP(w, r)
		log.Printf("%s %s %v", r.Method, r.URL.Path, time.Since(start))
	})
}

// newServer собирает *http.Server с роутингом и middleware.
func newServer(addr string) *http.Server {
	mux := http.NewServeMux()
	mux.HandleFunc("GET /users/{id}", handleUser)
	mux.HandleFunc("GET /health", handleHealth)

	return &http.Server{
		Addr:         addr,
		Handler:      loggingMiddleware(mux),
		ReadTimeout:  5 * time.Second,
		WriteTimeout: 10 * time.Second,
		IdleTimeout:  120 * time.Second,
	}
}

// run запускает сервер и завершает его gracefully при отмене ctx.
func run(ctx context.Context, srv *http.Server) error {
	errCh := make(chan error, 1)
	go func() {
		if err := srv.ListenAndServe(); err != nil && err != http.ErrServerClosed {
			errCh <- err
		}
	}()

	select {
	case err := <-errCh:
		return err
	case <-ctx.Done():
	}

	log.Println("shutting down...")
	shutdownCtx, cancel := context.WithTimeout(context.Background(), 30*time.Second)
	defer cancel()
	return srv.Shutdown(shutdownCtx)
}

func main() {
	ctx, stop := signal.NotifyContext(context.Background(), syscall.SIGINT, syscall.SIGTERM)
	defer stop()

	srv := newServer(":8080")
	log.Println("listening on", srv.Addr)
	if err := run(ctx, srv); err != nil {
		log.Fatalf("server: %v", err)
	}
	log.Println("server stopped")
}
