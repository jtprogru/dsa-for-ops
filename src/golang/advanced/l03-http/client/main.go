// HTTP-клиент с явным таймаутом и контекстом.
package main

import (
	"context"
	"fmt"
	"io"
	"log"
	"net/http"
	"time"
)

// fetch выполняет GET-запрос и возвращает статус и тело ответа.
func fetch(ctx context.Context, client *http.Client, url string) (int, string, error) {
	req, err := http.NewRequestWithContext(ctx, "GET", url, nil)
	if err != nil {
		return 0, "", err
	}
	resp, err := client.Do(req)
	if err != nil {
		return 0, "", err
	}
	defer resp.Body.Close()

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		return 0, "", err
	}
	return resp.StatusCode, string(body), nil
}

func main() {
	client := &http.Client{Timeout: 5 * time.Second}

	ctx, cancel := context.WithTimeout(context.Background(), 3*time.Second)
	defer cancel()

	status, body, err := fetch(ctx, client, "http://localhost:8080/users/42")
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println("статус:", status)
	fmt.Println("тело:  ", body)
}
