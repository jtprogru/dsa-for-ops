package main

import (
	"math"
	"testing"
)

func TestCircle(t *testing.T) {
	c := Circle{R: 2}
	if math.Abs(c.Area()-math.Pi*4) > 1e-9 {
		t.Errorf("Circle.Area() = %v", c.Area())
	}
	if math.Abs(c.Perimeter()-4*math.Pi) > 1e-9 {
		t.Errorf("Circle.Perimeter() = %v", c.Perimeter())
	}
}

func TestRectangle(t *testing.T) {
	r := Rectangle{W: 3, H: 4}
	if r.Area() != 12 {
		t.Errorf("Rectangle.Area() = %v, want 12", r.Area())
	}
	if r.Perimeter() != 14 {
		t.Errorf("Rectangle.Perimeter() = %v, want 14", r.Perimeter())
	}
}

func TestDescribe(t *testing.T) {
	describe(Circle{R: 1}) // smoke
	describe(Rectangle{W: 1, H: 1})
}

func TestAnyKind(t *testing.T) {
	cases := []struct {
		v    any
		want string
	}{
		{42, "int=42"},
		{"hi", `string="hi"`},
		{[]int{1, 2}, "[]int len=2"},
		{nil, "nil"},
		{3.14, "unknown type float64"},
	}
	for _, c := range cases {
		if got := anyKind(c.v); got != c.want {
			t.Errorf("anyKind(%v) = %q, want %q", c.v, got, c.want)
		}
	}
}

// TestSmoke проверяет, что демо запускается без паники.
func TestSmoke(t *testing.T) {
	main()
}
