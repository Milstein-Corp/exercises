package main

import "fmt"

func main() {
	var a01 TreeNode
	var a11 TreeNode
	//var a12 TreeNode
	//var a21 TreeNode
	//var a22 TreeNode
	//var a23 TreeNode
	//var a24 TreeNode

	a01.Left = &a11
	//a01.Right = &a12
	//a11.Left = &a21
	//a11.Right = &a22
	//a12.Left = &a23
	//a12.Right = &a24

	a01.Val = 1
	a11.Val = 1
	//a12.Val = 1
	//a21.Val = 1
	//a22.Val = 3
	//a23.Val = 6
	//a24.Val = 7

	var b01 TreeNode
	//var b11 TreeNode
	var b12 TreeNode
	//var b21 TreeNode
	//var b22 TreeNode
	//var b23 TreeNode
	//var b24 TreeNode

	b01.Left = nil//&b11
	b01.Right = &b12
	//b11.Left = &b21
	//b11.Right = &b22
	//b12.Left = &b23
	//b12.Right = &b24

	b01.Val = 1
	//b11.Val = 2
	b12.Val = 1
	//b21.Val = 1
	//b22.Val = 3
	//b23.Val = 6
	//b24.Val = 7

	fmt.Println(a01)
	fmt.Println(b01)

	fmt.Println(isSameTree(&a01, &b01))
}

func isSameTree(p *TreeNode, q *TreeNode) bool {
	aarray := make([]*int, 0, 10)
	barray:=make([]*int, 0, 0)
	aarray=traverseTree(p, aarray)
	barray=traverseTree(q, barray)
	fmt.Println(aarray)
	fmt.Println(barray)

	//for i:=0; i<len(aarray); i++ {
	//	p:=aarray[i]
	//	if(p==nil) {
	//		fmt.Println("nil")
	//	} else {
	//		fmt.Printf("*p=i=%v\n", *p)
	//	}
	//}

	return sameSlice(aarray, barray)
}

func traverseTree(node *TreeNode, rep []*int) []*int {
	if node == nil {
		//k:=-10
		rep=append(rep,nil)
		return rep
	}
	rep=append(rep, &node.Val)
	rep=traverseTree(node.Left, rep)

	rep=traverseTree(node.Right, rep)
	return rep
}

func sameSlice(slice1 []*int, slice2 []*int) bool {
	if len(slice1) != len(slice2) {
		return false
	}
	for i:=0; i < len(slice1); i++ {
		if slice1[i] == nil && slice2[i] == nil {

		} else if slice1[i] == nil || slice2[i] == nil {
			return false
		} else if *slice1[i]!=*slice2[i] {
			return false
		}
	}
	return true
}


// Definition for a binary tree node.
type TreeNode struct {
     Val int
     Left *TreeNode
     Right *TreeNode
 }
