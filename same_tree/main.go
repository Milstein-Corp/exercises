package main

import "fmt"

func main() {
	var a01 TreeNode
	var a11 TreeNode
	var a12 TreeNode
	var a21 TreeNode
	var a22 TreeNode
	var a23 TreeNode
	var a24 TreeNode

	a01.Left = &a11
	a01.Right = &a12
	a11.Left = &a21
	a11.Right = &a22
	a12.Left = &a23
	a12.Right = &a24

	a01.Val = 0
	a11.Val = 1
	a12.Val = 2
	a21.Val = 3
	a22.Val = 4
	a23.Val = 5
	a24.Val = 6

	traverseTree(a01)
}

func traverseTree(node TreeNode) {
	fmt.Println(node.Val)
}


// Definition for a binary tree node.
type TreeNode struct {
     Val int
     Left *TreeNode
     Right *TreeNode
 }

func superman() {
	fmt.Println("that")
}