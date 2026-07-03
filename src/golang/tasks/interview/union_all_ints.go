// Package interview — Go-версии задач с собеседований из tasks/interview
// Python-трека. Там структуры данных применяются на готовых dict/set/list,
// здесь — на map и срезах.
package interview

import "sort"

// UnionAllInts возвращает объединение всех переданных срезов: каждое число
// входит в результат один раз, порядок — по возрастанию. nil-срезы допустимы
// (range по nil безопасен), при пустом входе возвращается []int{}, а не nil.
func UnionAllInts(slices ...[]int) []int {
	seen := make(map[int]struct{})
	for _, s := range slices {
		for _, v := range s {
			seen[v] = struct{}{}
		}
	}
	res := make([]int, 0, len(seen))
	for v := range seen {
		res = append(res, v)
	}
	sort.Ints(res)
	return res
}
