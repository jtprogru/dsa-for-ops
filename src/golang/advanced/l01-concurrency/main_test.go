package main

import (
	"sync"
	"testing"
)

func TestWorker(t *testing.T) {
	jobs := make(chan int, 3)
	results := make(chan int, 3)
	for _, j := range []int{2, 3, 4} {
		jobs <- j
	}
	close(jobs)

	var wg sync.WaitGroup
	wg.Add(1)
	go worker(1, jobs, results, &wg)
	wg.Wait()
	close(results)

	sum := 0
	for r := range results {
		sum += r
	}
	if sum != 4+9+16 {
		t.Errorf("сумма квадратов = %d, want 29", sum)
	}
}

// TestSmoke проверяет, что демо worker pool отрабатывает без паники.
func TestSmoke(t *testing.T) {
	main()
}
