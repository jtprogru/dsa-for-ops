package main

import (
	"errors"
	"testing"
)

func TestDivide(t *testing.T) {
	q, err := divide(10, 2)
	if err != nil || q != 5 {
		t.Fatalf("divide(10, 2) = %v, %v; want 5, nil", q, err)
	}
	if _, err := divide(1, 0); !errors.Is(err, ErrDivideByZero) {
		t.Errorf("divide(1, 0) err = %v, want ErrDivideByZero", err)
	}
}

func TestCheckAge(t *testing.T) {
	if err := checkAge(30); err != nil {
		t.Errorf("checkAge(30) = %v, want nil", err)
	}
	var ve *ValidationError
	if err := checkAge(-1); !errors.As(err, &ve) {
		t.Errorf("checkAge(-1) err = %v, want *ValidationError", err)
	}
	if err := checkAge(200); !errors.As(err, &ve) {
		t.Errorf("checkAge(200) err = %v, want *ValidationError", err)
	}
}

func TestValidationErrorMessage(t *testing.T) {
	e := &ValidationError{Field: "age", Message: "плохо"}
	if got := e.Error(); got != "валидация age: плохо" {
		t.Errorf("Error() = %q", got)
	}
}

func TestCounter(t *testing.T) {
	next := counter()
	if a, b, c := next(), next(), next(); a != 1 || b != 2 || c != 3 {
		t.Errorf("counter дал %d, %d, %d; want 1, 2, 3", a, b, c)
	}
}

func TestRecoverable(t *testing.T) {
	if err := recoverable(); err == nil {
		t.Error("recoverable() = nil, ожидали ошибку после recover")
	}
}

// TestSmoke проверяет, что демо запускается без паники.
func TestSmoke(t *testing.T) {
	main()
}
