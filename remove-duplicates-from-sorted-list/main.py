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
        if not head:
            return None

        cur = head
        val = cur.val + 1
        prev = ListNode(1)
        dummy = prev
        prev.next = head
        print()
        print("BEFORE WHILE LOOP")
        printl(dummy, "dummy: ")
        printl(head, "head : ")
        while cur:
            print("DURING WHILE LOOP")
            # will we keep cur? prev is the end of the valid list.
            if cur.val == val:
                print("removing stuff")
                prev.next = cur.next
                cur.next = None
                cur = prev.next
            else:
                print("keepin stuff")
                val = cur.val
                cur = cur.next
                prev = prev.next
            printl(dummy, "dummy: ")
            printl(head, "head : ")
            print()
        print("AFTER WHILE LOOP")
        printl(dummy, "dummy: ")
        printl(head, "head : ")
        print()
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
