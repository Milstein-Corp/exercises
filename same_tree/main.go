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

	fmt.Println(a01)

	a01.Left = &a11
	a01.Right = &a12
	a11.Left = &a21
	a11.Right = nil//&a22
	a12.Left = &a23
	a12.Right = &a24

	a01.Val = 4
	a11.Val = 2
	a12.Val = 5
	a21.Val = 1
	a22.Val = 3
	a23.Val = 6
	a24.Val = 7

	aarray := make([]int, 0, 10)
	aarray=traverseTree(&a01, aarray)

	var b01 TreeNode
	var b11 TreeNode
	var b12 TreeNode
	var b21 TreeNode
	var b22 TreeNode
	var b23 TreeNode
	var b24 TreeNode

	b01.Left = &b11
	b01.Right = &b12
	b11.Left = &b21
	b11.Right = &b22
	b12.Left = &b23
	b12.Right = &b24

	b01.Val = -4
	b11.Val = -2
	b12.Val = -5
	b21.Val = -1
	b22.Val = -3
	b23.Val = -6
	b24.Val = -7

	barray:=make([]int, 0, 0)
	barray=traverseTree(&b01, barray)

	fmt.Println("after traversal")
	fmt.Println(barray)
	fmt.Println(len(barray))
	fmt.Println(cap(barray))
	fmt.Println("after traversal")
	fmt.Println(aarray)
	fmt.Println(len(aarray))
	fmt.Println(cap(aarray))
}

func traverseTree(node *TreeNode, rep []int) []int {
	if node == nil {
		return rep
	}
	rep=traverseTree(node.Left, rep)
	rep=append(rep, node.Val)
	fmt.Println(node.Val)
	rep=traverseTree(node.Right, rep)

	return rep
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