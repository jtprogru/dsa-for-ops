package main

import (
	"context"
	"net/http"
	"net/http/httptest"
	"testing"
	"time"
)

func TestFetch(t *testing.T) {
	srv := httptest.NewServer(http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusOK)
		_, _ = w.Write([]byte("привет"))
	}))
	defer srv.Close()

	status, body, err := fetch(context.Background(), srv.Client(), srv.URL)
	if err != nil {
		t.Fatalf("fetch error: %v", err)
	}
	if status != http.StatusOK {
		t.Errorf("status = %d, want 200", status)
	}
	if body != "привет" {
		t.Errorf("body = %q, want привет", body)
	}
}

func TestFetchError(t *testing.T) {
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Millisecond)
	defer cancel()
	// Порт 0 недоступен для подключения — ожидаем ошибку.
	if _, _, err := fetch(ctx, &http.Client{Timeout: 10 * time.Millisecond}, "http://127.0.0.1:0"); err == nil {
		t.Error("ожидали ошибку для недоступного адреса")
	}
}
