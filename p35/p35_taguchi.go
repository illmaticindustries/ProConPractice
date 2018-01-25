package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var file, _ = os.Open(`./p35_case3.in`)
var sc = bufio.NewScanner(file)

func nextLine() string {
	sc.Scan()
	return sc.Text()
}

var n, _ = strconv.Atoi(nextLine())
var m, _ = strconv.Atoi(nextLine())

func splitYard() [][]string {
	y := make([]string, n)
	a := make([][]string, 0)
	for i := 0; i < n; i++ {
		y = strings.Split(nextLine(), "")
		a = append(a, y)
	}
	return a
}

var yard = splitYard()

func dfs(x int, y int) {
	yard[x][y] = "."
	for dx := -1; dx <= 1; dx++ {
		for dy := -1; dy <= 1; dy++ {
			nx := x + dx
			ny := y + dy
			if 0 <= nx && nx < n && 0 <= ny && ny < m && yard[nx][ny] == "W" {
				dfs(nx, ny)
			}
		}
	}
}

var count = 0

func main() {
	for x := 0; x < n; x++ {
		for y := 0; y < m; y++ {
			if yard[x][y] == "W" {
				dfs(x, y)
				count++
			}
		}
	}
	fmt.Print(count)
}
