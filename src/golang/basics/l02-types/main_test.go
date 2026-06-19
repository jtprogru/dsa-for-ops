package main

import "testing"

func TestClassify(t *testing.T) {
	cases := map[int]string{-5: "отрицательное", 0: "ноль", 7: "положительное"}
	for n, want := range cases {
		if got := classify(n); got != want {
			t.Errorf("classify(%d) = %q, want %q", n, got, want)
		}
	}
}

func TestSumTo(t *testing.T) {
	if got := sumTo(10); got != 55 {
		t.Errorf("sumTo(10) = %d, want 55", got)
	}
	if got := sumTo(0); got != 0 {
		t.Errorf("sumTo(0) = %d, want 0", got)
	}
}

func TestWeekdayString(t *testing.T) {
	if got := Friday.String(); got != "Пт" {
		t.Errorf("Friday.String() = %q, want Пт", got)
	}
	if got := Sunday.String(); got != "Вс" {
		t.Errorf("Sunday.String() = %q, want Вс", got)
	}
}

// TestSmoke проверяет, что демо запускается без паники.
func TestSmoke(t *testing.T) {
	main()
}
