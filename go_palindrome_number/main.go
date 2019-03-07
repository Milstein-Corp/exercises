package main

import (
	"fmt"
	"strconv"
)

func main() {
	var x int = 505

	fmt.Println(isPalindrome(x))
}

func isPalindrome(x int) bool {
	var y string
	//var half string
	var right int
	var isPal bool

	y = strconv.Itoa(x)
	right = len(y) - 1
	isPal = true
	//half = y[:right/2 + 1] //this improvement is substantially slower and more memory intensive

	for left := range y {
		leftValue := y[left]
		rightValue := y[right]

		if leftValue != rightValue {
			isPal = false
		}

		fmt.Printf("left index: %v   right index: %v\n",left,right)
		fmt.Printf("left value: %v   right value: %v\n",leftValue, rightValue)

		right -= 1
	}

	return isPal
}
