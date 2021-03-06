package main

import "fmt"

func main() {
	var a ListNodeq
	var b ListNode
	var c ListNode

	a.Val = 1
	b.Val = 3
	c.Val = 3
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

	fmt.Println("The result is: ")
	for g != nil {
		fmt.Println(g.Val)
		g = g.Next
	}
}

type ListNode struct{
	Val int
	Next *ListNode
}

func mergeTwo(l1 *ListNode, l2 *ListNode) *ListNode {
	//preprocess.

	var last *ListNode
	var first ListNode
	last = &first

	//advance through the body
	for l1 != nil && l2 != nil {
		if l2.Val < l1.Val {
			last.Next = l2
			l2 = l2.Next
		} else {
			last.Next = l1
			l1 = l1.Next
		}
		last = last.Next
		last.Next = nil
	}

	//final condition. One or both is nil
	if l1 != nil {
		last.Next = l1
		l1 = nil
	} else if l2 != nil {
		last.Next = l2
		l2 =nil
	}

	return first.Next
}

func mergeTwoFirstAttempt(l1 *ListNode, l2 *ListNode) *ListNode {
	//preprocess. Well, we are guaranteed that neither is nil
	if l1 == nil {
		return l2
	} else if l2 == nil {
		return l1
	}
	var last *ListNode
	var first *ListNode
	if l2.Val < l1.Val {
		last = l2
		l2 = l2.Next
	} else {
		last = l1
		l1 = l1.Next
	}
	last.Next = nil
	first = last

	//advance through the body
	for l1 != nil && l2 != nil {
		fmt.Printf("last val is: %v\n",last.Val)
		fmt.Printf("l1 val is: %v\n", l1.Val)
		fmt.Printf("l2 val is: %v\n\n", l2.Val)
		if l2.Val < l1.Val {
			last.Next = l2
			l2 = l2.Next
		} else {
			last.Next = l1
			l1 = l1.Next
		}
		last = last.Next
		last.Next = nil
	}

	fmt.Printf("last val is: %v\n",last.Val)
	fmt.Printf("l1 val is nil: %v\n", l1==nil)
	fmt.Printf("l2 val is nil: %v\n\n", l2==nil)
	//final condition. One ref is nil
	if l1 == nil {
		last.Next = l2
	} else {
		last.Next = l1
	}
	return first
}
