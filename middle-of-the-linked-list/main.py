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
    def middleNode(self, head):
        if not head:
            return None
        if not head.next:
            return head

        n = 0
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            n = n + 1

        if fast and not fast.next:
            # 1 + 2n nodes
            return slow

        if not fast:
            # fast points at 1 + 2n, but, 2n nodes.
            return slow


if __name__ == '__main__':
    print("CASE")
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3.5)
    a.next.next.next = ListNode(3)
    a.next.next.next.next = ListNode(2)
    # a.next.next.next.next.next = ListNode(1)
    printl(a, "argument: ")
    actual = Solution.middleNode(Solution, a)
    printl(a, "argument: ")
    print(actual.val)



