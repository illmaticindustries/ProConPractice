package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

var sc = bufio.NewScanner(os.Stdin)

func nextLine() string {
	sc.Scan()
	return sc.Text()
}

type Coin struct {
	Price int
	Num   int
}

func nextCoin() int {
	var c, _ = strconv.Atoi(nextLine())
	return c
}

func getCoins() []Coin {
	a := make([]Coin, 0)
	a = append(a, Coin{1, nextCoin()}, Coin{5, nextCoin()}, Coin{10, nextCoin()}, Coin{50, nextCoin()}, Coin{100, nextCoin()}, Coin{500, nextCoin()})
	return a
}

var coins = getCoins()
var sum, _ = strconv.Atoi(nextLine())

func main() {
	result := make([][]int, 0)
	for range coins {
		coin := coins[len(coins)-1]
		coins = coins[:len(coins)-1]
		var use_num = 0
		if sum/coin.Price >= coin.Num {
			use_num = coin.Num
		} else {
			use_num = sum / coin.Price
		}
		sum -= use_num * coin.Price
		coin_result := make([]int, 0)
		coin_result = append(coin_result, coin.Price, use_num)
		result = append(result, coin_result)
	}
	for _, r := range result {
		fmt.Printf("%d円%d枚\n", r[0], r[1])
	}
}
