package main

import "fmt"

func main() {
	fmt.Println("this is the way")
	var a ListNode
	var b ListNode
	var c ListNode
	a.Val = 1
	b.Val = 3
	c.Val = 5
	a.Next = &b
	b.Next = &c

	var d ListNode
	var e ListNode
	var f ListNode
	d.Val = 2
	e.Val = 4
	f.Val = 6
	d.Next = &e
	e.Next = &f

	g := mergeTwo(&a, &d)
	fmt.Printf("function returns: %v\n", g.Val)
}

type ListNode struct{
	Val int
	Next *ListNode
}

func mergeTwo(l1 *ListNode, l2 *ListNode) *ListNode {
	//preprocess
	if l1 == nil {
		return l2
	} else if l2 == nil {
		return l1
	}

	var last *ListNode
	var first *ListNode

	if l2.Val > l1.Val {
		last = l2
		l2 = l2.Next
	} else {
		last = l1
		l1 = l1.Next
	}

	last.Next = nil
	first = last

	fmt.Printf("list one value: %v\n", l1.Val)
	fmt.Printf("list two value: %v\n", l2.Val)

	var curr *ListNode
	curr = l1

	for curr != nil {
		fmt.Println(curr.Val)
		curr = curr.Next
	}

	var l ListNode
	l.Val = 3
	return first
}
