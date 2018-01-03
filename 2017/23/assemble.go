package main

import "fmt"
import "os"
import "bufio"
import "strings"
import "strconv"

func ReadCmds(fname string) [][]string {
	file, err := os.Open(fname)
	if err != nil {
		panic(err)
	}
	defer file.Close()
	reader := bufio.NewReader(file)
	cmds := make([][]string, 0)
	for {
		line, err := reader.ReadString('\n')
		if err != nil {
			break
		}
		cmds = append(cmds, strings.Fields(line))
	}
	return cmds
}

func Parse(memory map[string]int, x string) int {
	y, ok := memory[x]
	if ok {
		return y
	}

	y, err := strconv.Atoi(x)
	if err != nil {
		panic(err)
	}
	return y
}

func ClearMemory(memory map[string]int) {
	for x := int('a'); x <= int('h'); x++ {
		memory[string(x)] = 0
	}
}

func PrintMemory(memory map[string]int) {
	for x := int('a'); x <= int('h'); x++ {
		fmt.Printf("%v: %8d  ", string(x), memory[string(x)])
	}
	fmt.Println()
}

func RunPart1(cmds [][]string, memory map[string]int) int {
	var count_mul int
	for i := 0; i >= 0 && i < len(cmds); i++ {
		switch cmds[i][0] {
		case "set":
			memory[cmds[i][1]] = Parse(memory, cmds[i][2])
		case "add":
			memory[cmds[i][1]] += Parse(memory, cmds[i][2])
		case "sub":
			memory[cmds[i][1]] -= Parse(memory, cmds[i][2])
		case "mul":
			memory[cmds[i][1]] *= Parse(memory, cmds[i][2])
			count_mul += 1
		case "mod":
			memory[cmds[i][1]] %= Parse(memory, cmds[i][2])
		case "jnz":
			if Parse(memory, cmds[i][1]) != 0 {
				i += Parse(memory, cmds[i][2]) - 1
			}
		default:
			fmt.Printf("Could not parse: %s\n", cmds[i][0])
			return count_mul
		}
	}

	return count_mul
}

func RunPart2(cmds [][]string, memory map[string]int) int {
	var count_jnz int
	for i := 0; i >= 0 && i < len(cmds); i++ {
		switch cmds[i][0] {
		case "set":
			memory[cmds[i][1]] = Parse(memory, cmds[i][2])
		case "add":
			memory[cmds[i][1]] += Parse(memory, cmds[i][2])
		case "sub":
			memory[cmds[i][1]] -= Parse(memory, cmds[i][2])
		case "mul":
			memory[cmds[i][1]] *= Parse(memory, cmds[i][2])
		case "mod":
			memory[cmds[i][1]] %= Parse(memory, cmds[i][2])
		case "jnz":
			fmt.Printf("%2d: %3v  ", i, cmds[i])
			PrintMemory(memory)
			if Parse(memory, cmds[i][1]) != 0 {
				i += Parse(memory, cmds[i][2]) - 1
			}
			count_jnz += 1
			if count_jnz == 100 {
				return count_jnz
			}
		default:
			fmt.Printf("Could not parse: %s\n", cmds[i][0])
			return count_jnz
		}
	}

	fmt.Println("Finished")

	return count_jnz
}

func main() {

	cmds := ReadCmds(os.Args[1])

	memory := make(map[string]int)
	ClearMemory(memory)

	c := RunPart1(cmds, memory)
	fmt.Printf("Part 1: count mul = %d\n", c)

	// ClearMemory(memory)
	// memory["a"] = 1
	// PrintMemory(memory)
	// RunPart2(cmds, memory)
}
