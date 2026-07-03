package interview

import (
	"reflect"
	"testing"
)

func TestUnionAllInts(t *testing.T) {
	tests := []struct {
		name   string
		slices [][]int
		want   []int
	}{
		{"три среза с пересечениями", [][]int{{1, 2, 3}, {3, 4}, {2, 5}}, []int{1, 2, 3, 4, 5}},
		{"без аргументов", nil, []int{}},
		{"nil-срез среди входа", [][]int{nil, {1, 1, 2}}, []int{1, 2}},
		{"все срезы пустые", [][]int{{}, {}}, []int{}},
		{"один срез", [][]int{{7}}, []int{7}},
		{"отрицательные и сортировка", [][]int{{3, -1}, {0, 3}, {-1}}, []int{-1, 0, 3}},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := UnionAllInts(tt.slices...)
			// DeepEqual различает nil и []int{} — заодно проверяем, что при
			// пустом входе возвращается именно пустой срез, а не nil.
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("UnionAllInts(%v) = %v, want %v", tt.slices, got, tt.want)
			}
		})
	}
}
