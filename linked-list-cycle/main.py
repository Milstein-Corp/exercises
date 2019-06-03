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
    def hasCycle(self, head):
        df = defaultdict()
        cur = head
        n = 1
        while cur:
            if not df.get(cur): # 1 is a true, 0 is the false
                df[cur] = n
            else:
                return True
            n += 1
            cur = cur.next

        return False


if __name__ == '__main__':
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(3)
    a.next.next.next.next = ListNode(2)
    a.next.next.next.next.next = ListNode(1)
    printl(a, "argument: ")
    actual = Solution.hasCycle(Solution, a)
    printl(a, "argument: ")
    print("answer: %s " % actual)
    print()
