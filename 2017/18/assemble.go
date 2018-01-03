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
	for x := int('a'); x <= int('z'); x++ {
		memory[string(x)] = 0
	}
}

func RunPart1(cmds [][]string, memory map[string]int) {
	var sound int

	for i := 0; i >= 0 && i < len(cmds); i++ {
		switch cmds[i][0] {
		case "set":
			memory[cmds[i][1]] = Parse(memory, cmds[i][2])
		case "add":
			memory[cmds[i][1]] += Parse(memory, cmds[i][2])
		case "mul":
			memory[cmds[i][1]] *= Parse(memory, cmds[i][2])
		case "mod":
			memory[cmds[i][1]] %= Parse(memory, cmds[i][2])
		case "snd":
			sound = Parse(memory, cmds[i][1])
		case "rcv":
			if Parse(memory, cmds[i][1]) != 0 {
				fmt.Printf("Recovering sound: %d\n", sound)
				return
			}
		case "jgz":
			if Parse(memory, cmds[i][1]) > 0 {
				i += Parse(memory, cmds[i][2]) - 1
			}
		default:
			fmt.Printf("Could not parse: %s\n", cmds[i][0])
			return
		}
	}
}

func RunPart2(cmds [][]string, memory map[string]int, p int, in chan int, out chan int, log chan string) {
	memory["p"] = p
	for i := 0; i >= 0 && i < len(cmds); i++ {
		switch cmds[i][0] {
		case "set":
			memory[cmds[i][1]] = Parse(memory, cmds[i][2])
		case "add":
			memory[cmds[i][1]] += Parse(memory, cmds[i][2])
		case "mul":
			memory[cmds[i][1]] *= Parse(memory, cmds[i][2])
		case "mod":
			memory[cmds[i][1]] %= Parse(memory, cmds[i][2])
		case "snd":
			v := Parse(memory, cmds[i][1])
			out <- v
			log <- fmt.Sprintf("ID: %d, Sent %d", p, v)
		case "rcv":
			v := <-in
			// log <- fmt.Sprintf("ID: %d, Received %d", p, v)
			memory[cmds[i][1]] = v
		case "jgz":
			if Parse(memory, cmds[i][1]) > 0 {
				i += Parse(memory, cmds[i][2]) - 1
			}
		default:
			fmt.Printf("Could not parse: %s\n", cmds[i][0])
			return
		}
	}
}

func main() {

	cmds := ReadCmds(os.Args[1])

	memory0 := make(map[string]int)

	ClearMemory(memory0)
	RunPart1(cmds, memory0)

	ClearMemory(memory0)
	memory1 := make(map[string]int)
	ClearMemory(memory1)

	C01 := make(chan int, 10000)
	C10 := make(chan int, 10000)

	log0 := make(chan string, 10000)
	log1 := make(chan string, 10000)

	go RunPart2(cmds, memory0, 0, C01, C10, log0)
	go RunPart2(cmds, memory1, 1, C10, C01, log1)

	p1_sends := 0
	for _ = range log1 {
		p1_sends += 1
		fmt.Printf("p1 sends: %d\n", p1_sends)
	}

	fmt.Println(p1_sends)

}
