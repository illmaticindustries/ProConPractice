package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var file, _ = os.Open(`./p37.in`)
var sc = bufio.NewScanner(file)

func nextLine() string {
	sc.Scan()
	return sc.Text()
}

var n, _ = strconv.Atoi(nextLine())
var m, _ = strconv.Atoi(nextLine())

func splitMaze() [][]string {
	m := make([]string, n)
	a := make([][]string, 0)
	for i := 0; i < n; i++ {
		m = strings.Split(nextLine(), "")
		a = append(a, m)
	}
	return a
}

var maze = splitMaze()

func searchStartGoal(coord string) []int {
	a := make([]int, 0)
	for x := 0; x < n; x++ {
		for y := 0; y < m; y++ {
			if maze[x][y] == coord {
				a = append(a, x, y)
			}
		}
	}
	return a
}

var start = searchStartGoal("S")
var goal = searchStartGoal("G")
var inf = 10000

func initDistance() [][]int {
	d := make([][]int, 0)
	for x := 0; x < n; x++ {
		a := make([]int, 0)
		for y := 0; y < m; y++ {
			a = append(a, inf)
		}
		d = append(d, a)
	}
	return d
}

var distance = initDistance()

func initQueue() [][]int {
	q := make([][]int, 0)
	q1 := []int{start[0], start[1]}
	q = append(q, q1)
	return q
}

var queue = initQueue()

func main() {
	distance[start[0]][start[1]] = 0
	dx := []int{1, 0, -1, 0}
	dy := []int{0, 1, 0, -1}
	for len(queue) > 0 {
		current := make([]int, 0)
		current, queue = queue[0], queue[1:]
		if current[0] == goal[0] && current[1] == goal[1] {
			break
		}
		for i := 0; i <= 3; i++ {
			nx := current[0] + dx[i]
			ny := current[1] + dy[i]
			if 0 <= nx && nx < n && 0 <= ny && ny < m && maze[nx][ny] != "#" && distance[nx][ny] == inf {
				n := make([]int, 0)
				n = append(n, nx, ny)
				queue = append(queue, n)
				distance[nx][ny] = distance[current[0]][current[1]] + 1
			}
		}
	}
	fmt.Print(distance[goal[0]][goal[1]])
}
