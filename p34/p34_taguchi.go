// go fmt && go run p34_taguchi.go
package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

var file, _ = os.Open(`./p34.in`)
var sc = bufio.NewScanner(file)

func nextLine() string {
	sc.Scan()
	return sc.Text()
}

var n, _ = strconv.Atoi(nextLine())
var sa = strings.Split(nextLine(), ",")
var a = sliceAtoi(sa)

func sliceAtoi(sa []string) []int {
	si := make([]int, 0, len(sa))
	for _, s := range sa {
		i, _ := strconv.Atoi(s)
		si = append(si, i)
	}
	return si
}

var k, _ = strconv.Atoi(nextLine())

func check(i int, sum int) bool {
	if i == n {
		return k == sum
	} else if check(i+1, sum+a[i]) {
		return true
	} else if check(i+1, sum) {
		return true
	}
	return false
}

func main() {
	if check(0, 0) {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
