package main

import "testing"

func TestAnimalGreet(t *testing.T) {
	a := &Animal{Name: "Барсик"}
	a.Greet() // smoke: не должно паниковать
}

func TestDogEmbedding(t *testing.T) {
	d := Dog{Animal: Animal{Name: "Рекс"}, Breed: "лабрадор"}
	if d.Name != "Рекс" || d.Breed != "лабрадор" {
		t.Errorf("embedding: Name=%q Breed=%q", d.Name, d.Breed)
	}
}

// TestSmoke проверяет, что демо запускается без паники.
func TestSmoke(t *testing.T) {
	main()
}
