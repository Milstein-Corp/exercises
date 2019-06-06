# Definition for singly-linked list.
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
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next


if __name__ == '__main__':
    print("CASE")
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(3)
    a.next.next.next.next = ListNode(2)
    a.next.next.next.next.next = ListNode(1)
    printl(a, "argument: ")
    Solution.deleteNode(Solution, a.next)
    printl(a, "argument: ")



