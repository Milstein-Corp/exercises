# Definition for singly-linked list.
from collections import defaultdict


def printl(l, header):
    cur = l
    print(header, end=": ")
    while cur:
        print(cur.val, end=", ")
        cur = cur.next
    print()


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):

        # cur is a keeper, cur.next is under question
        cur = head

        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next

        return head


if __name__ == '__main__':
    print("CASE")
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(3)
    a.next.next.next.next = ListNode(2)
    a.next.next.next.next.next = ListNode(1)
    printl(a, "argument: ")
    actual = Solution.deleteDuplicates(Solution, a)
    printl(a, "argument: ")
    printl(actual, "answer  : ")
    print()

    print("CASE")
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(3)
    a.next.next.next.next = ListNode(3)
    a.next.next.next.next.next = ListNode(3)
    printl(a, "argument: ")
    actual = Solution.deleteDuplicates(Solution, a)
    printl(a, "argument: ")
    printl(actual, "answer  : ")
    print()


    print("CASE")
    a = ListNode(1)
    a.next = ListNode(1)
    printl(a, "argument: ")
    actual = Solution.deleteDuplicates(Solution, a)
    printl(a, "argument: ")
    printl(actual, "answer  : ")
    print()


    print("CASE")
    a = ListNode(1)
    a.next = ListNode(1)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(3)
    a.next.next.next.next = ListNode(3)
    a.next.next.next.next.next = ListNode(3)
    printl(a, "argument: ")
    actual = Solution.deleteDuplicates(Solution, a)
    printl(a, "argument: ")
    printl(actual, "answer  : ")
    print()

    print("CASE")
    a = ListNode(0)
    a.next = ListNode(0)
    a.next.next = ListNode(0)
    a.next.next.next = ListNode(0)
    a.next.next.next.next = ListNode(0)
    a.next.next.next.next.next = ListNode(0)
    printl(a, "argument: ")
    actual = Solution.deleteDuplicates(Solution, a)
    printl(a, "argument: ")
    printl(actual, "answer  : ")
    print()

    print("CASE")
    a = ListNode(1)
    a.next = ListNode(1)
    a.next.next = ListNode(1)
    a.next.next.next = ListNode(1)
    a.next.next.next.next = ListNode(1)
    a.next.next.next.next.next = ListNode(1)
    printl(a, "argument: ")
    actual = Solution.deleteDuplicates(Solution, a)
    printl(a, "argument: ")
    printl(actual, "answer  : ")
    print()
