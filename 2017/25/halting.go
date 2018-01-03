package main

import "fmt"

func step_example(state rune, tape map[int]bool, cursor int) (rune, int) {
	switch state {
	case 'A':
		_, ok := tape[cursor]
		if !ok {
			tape[cursor] = true
			cursor += 1
		} else {
			delete(tape, cursor)
			cursor -= 1
		}
		state = 'B'
	case 'B':
		_, ok := tape[cursor]
		if !ok {
			tape[cursor] = true
			cursor -= 1
		} else {
			cursor += 1
		}
		state = 'A'
	}

	return state, cursor
}

func step_input(state rune, tape map[int]bool, cursor int) (rune, int) {
	_, ok := tape[cursor]
	switch state {
	case 'A':
		if !ok {
			tape[cursor] = true
			cursor += 1
			state = 'B'
		} else {
			delete(tape, cursor)
			cursor -= 1
			state = 'C'
		}
	case 'B':
		if !ok {
			tape[cursor] = true
			cursor -= 1
			state = 'A'
		} else {
			cursor -= 1
			state = 'D'
		}
	case 'C':
		if !ok {
			tape[cursor] = true
			cursor += 1
			state = 'D'
		} else {
			delete(tape, cursor)
			cursor += 1
			state = 'C'
		}
	case 'D':
		if !ok {
			cursor -= 1
			state = 'B'
		} else {
			delete(tape, cursor)
			cursor += 1
			state = 'E'
		}
	case 'E':
		if !ok {
			tape[cursor] = true
			cursor += 1
			state = 'C'
		} else {
			cursor -= 1
			state = 'F'
		}
	case 'F':
		if !ok {
			tape[cursor] = true
			cursor -= 1
			state = 'E'
		} else {
			cursor += 1
			state = 'A'
		}
	}

	return state, cursor
}

func Checksum(tape map[int]bool) {
	// Count number of keys in tape
	count := 0
	for _ = range tape {
		count += 1
	}
	fmt.Printf("Diagnostic Checksum: %d\n", count)
}

func main() {
	var state rune
	var cursor int
	var tape map[int]bool

	// Part 1
	state = 'A'
	tape = make(map[int]bool)
	cursor = 0
	for i := 0; i < 6; i++ {
		state, cursor = step_example(state, tape, cursor)

		fmt.Printf("State: %d, %v\n", state, cursor)
		for key, _ := range tape {
			fmt.Printf("%d ", key)
		}
		fmt.Println()
	}
	Checksum(tape)

	// Part 2
	state = 'A'
	tape = make(map[int]bool)
	cursor = 0
	for i := 0; i < 12172063; i++ {
		state, cursor = step_input(state, tape, cursor)
	}

	Checksum(tape)
}
