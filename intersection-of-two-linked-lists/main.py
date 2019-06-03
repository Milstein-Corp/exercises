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
    def getIntersectionNode(self, headA, headB):

        cura = headA
        curb = headB

        while cura != curb:
            if cura is not None:
                cura = cura.next
            else:
                cura = headB

            if curb is not None:
                curb = curb.next
            else:
                curb = headA


        return cura


if __name__ == '__main__':
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(3)
    a.next.next.next.next = ListNode(2)
    a.next.next.next.next.next = ListNode(1)
    b = ListNode(1)
    b.next = ListNode(2)
    b.next.next = ListNode(3)
    b.next.next.next = ListNode(3)
    b.next.next.next.next = ListNode(2)
    b.next.next.next.next.next = ListNode(1)
    printl(a, "argument: ")
    actual = Solution.getIntersectionNode(Solution, a, b)
    printl(a, "argument: ")
    if actual:
        print(actual.val)
    else:
        print(actual)
    print()

    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    b = ListNode(1)
    b.next = a.next
    printl(a, "argument a: ")
    printl(b, "argument b: ")
    actual = Solution.getIntersectionNode(Solution, a, b)
    printl(a, "argument a: ")
    printl(b, "argument b: ")
    if actual:
        print("shared value is: %s " % actual.val)
    else:
        print(actual)
    print()

    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(3)
    a.next.next.next.next = ListNode(22)
    a.next.next.next.next.next = ListNode(1)
    b = ListNode(10)
    b.next = ListNode(11)
    b.next.next = ListNode(12)
    b.next.next.next = a.next.next.next.next

    printl(a, "argument a: ")
    printl(b, "argument b: ")
    actual = Solution.getIntersectionNode(Solution, a, b)
    printl(a, "argument a: ")
    printl(b, "argument b: ")
    if actual:
        print("shared value is: %s " % actual.val)
    else:
        print(actual)

    print()
    #
#