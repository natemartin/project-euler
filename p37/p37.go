package main

import (
	"fmt"
	"strconv"
)

var keys []int
var primes map[int]bool

func main() {
	primes = map[int]bool{}
	primes[2] = true
	keys = append(keys, 2)
	for i := 3; i < 1000000; i += 2 {
		for _, j := range keys {
			if i%j == 0 {
				break
			}
			if j*j >= i {
				keys = append(keys, i)
				primes[int(i)] = true
				break
			}
		}
	}
	sum := 0
	for _, i := range keys {
		if is_truncatable(i) {
			sum += i
		}
	}
	fmt.Println(sum)
}

func is_truncatable(x int) bool {
	x_str := strconv.Itoa(x)
	if len(x_str) < 2 {
		return false
	}
	for i := 0; i < len(x_str); i++ {
		sub := x_str[:len(x_str)-i]
		sub2 := x_str[i:]
		i, _ := strconv.ParseInt(sub, 10, 32)
		j, _ := strconv.ParseInt(sub2, 10, 32)
		if !primes[int(i)] || !primes[int(j)] {
			return false
		}
	}
	return true
}
