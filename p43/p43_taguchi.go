package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
)

var sc = bufio.NewScanner(os.Stdin)

func nextLine() string {
	sc.Scan()
	return sc.Text()
}

var n, _ = strconv.Atoi(nextLine())
var s = getArray()
var t = getArray()

func getArray() []int {
	a := make([]int, 0)
	for i := 0; i < n; i++ {
		j, _ := strconv.Atoi(nextLine())
		a = append(a, j)
	}
	return a
}

var itv = getItv()

func getItv() [][]int {
	itv := make([][]int, 0)
	for i := 0; i < n; i++ {
		a := make([]int, 0)
		a = append(a, t[i])
		a = append(a, s[i])
		itv = append(itv, a)
	}
	sort.Slice(itv, func(i, j int) bool { return itv[i][0] < itv[j][0] })
	return itv
}
func main() {
	ans, u := 0, 0
	for i := 0; i < n; i++ {
		if u < itv[i][1] {
			ans++
			u = itv[i][0]
		}
	}
	fmt.Println(ans)
}
