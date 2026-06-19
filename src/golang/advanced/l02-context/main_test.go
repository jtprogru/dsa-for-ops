package main

import (
	"context"
	"testing"
	"time"
)

func TestSlowWorkCompletes(t *testing.T) {
	if err := slowWork(context.Background(), "test", 10*time.Millisecond); err != nil {
		t.Errorf("slowWork завершилась с ошибкой: %v", err)
	}
}

func TestSlowWorkCancelled(t *testing.T) {
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Millisecond)
	defer cancel()
	if err := slowWork(ctx, "test", 1*time.Second); err == nil {
		t.Error("slowWork должна вернуть ошибку при отмене контекста")
	}
}

// TestSmoke проверяет, что демо отрабатывает без паники.
func TestSmoke(t *testing.T) {
	main()
}
