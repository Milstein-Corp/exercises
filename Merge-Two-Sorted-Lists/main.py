# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None

        mnode = ListNode(-1)
        mnode.next = head
        mind = 0
        while mind < m-1:
            mnode = mnode.next
            mind += 1

        nnode = head
        nind = 1
        while nind < n + 1:
            nnode = nnode.next
            nind += 1

        rest = mnode.next
        growing = None
        moved = 0

        while rest and moved < n - m + 1:
            move = rest
            rest = rest.next
            move.next = growing
            growing = move
            moved += 1

        mnode.next = growing

        cur = mnode
        while cur.next:
            cur = cur.next
        cur.next = nnode
        if m == 1:
            return growing
        else:
            return head


if __name__ == '__main__':
    head = ListNode(0)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(4)
    head.next.next.next.next.next = ListNode(5)
    head.next.next.next.next.next.next = ListNode(6)

    m = 2
    n = 4
    expected = ListNode(0)
    expected.next = ListNode(3)
    expected.next.next = ListNode(2)
    expected.next.next.next = ListNode(1)
    expected.next.next.next.next = ListNode(4)
    expected.next.next.next.next.next = ListNode(5)
    expected.next.next.next.next.next.next = ListNode(6)

    print("m: %s, n: %s" % (m, n))
    print("argument: ", end=" ")
    cur = head
    while cur:
        print(cur.val, end=", ")
        cur = cur.next
    print()
    print("expected: ", end=" ")
    cur = expected
    while cur:
        print(cur.val, end=", ")
        cur = cur.next
    print()
    actual = Solution.reverseBetween(Solution, head, m, n)
    print("actual: ", end=" ")
    cur = actual
    while cur:
        print(cur.val, end=", ")
        cur = cur.next
    print()
    print()

####

    head = ListNode(0)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(4)
    head.next.next.next.next.next = ListNode(5)
    head.next.next.next.next.next.next = ListNode(6)

    m = 2
    n = 7
    expected = ListNode(0)
    expected.next = ListNode(6)
    expected.next.next = ListNode(5)
    expected.next.next.next = ListNode(4)
    expected.next.next.next.next = ListNode(3)
    expected.next.next.next.next.next = ListNode(2)
    expected.next.next.next.next.next.next = ListNode(1)

    print("m: %s, n: %s" % (m, n))
    print("argument: ", end=" ")
    cur = head
    while cur:
        print(cur.val, end=", ")
        cur = cur.next
    print()
    print("expected: ", end=" ")
    cur = expected
    while cur:
        print(cur.val, end=", ")
        cur = cur.next
    print()
    actual = Solution.reverseBetween(Solution, head, m, n)
    print("actual: ", end=" ")
    cur = expected
    while cur:
        print(cur.val, end=", ")
        cur = cur.next
    print()
    print()

####

    head = ListNode(0)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    head.next.next.next = ListNode(3)
    head.next.next.next.next = ListNode(4)
    head.next.next.next.next.next = ListNode(5)
    head.next.next.next.next.next.next = ListNode(6)

    m = 1
    n = 7
    expected = ListNode(6)
    expected.next = ListNode(5)
    expected.next.next = ListNode(4)
    expected.next.next.next = ListNode(3)
    expected.next.next.next.next = ListNode(2)
    expected.next.next.next.next.next = ListNode(1)
    expected.next.next.next.next.next.next = ListNode(0)

    print("m: %s, n: %s" % (m, n))
    print("argument: ", end=" ")
    cur = head
    while cur:
        print(cur.val, end=", ")
        cur = cur.next
    print()
    print("expected: ", end=" ")
    cur = expected
    while cur:
        print(cur.val, end=", ")
        cur = cur.next
    print()
    actual = Solution.reverseBetween(Solution, head, m, n)
    print("actual: ", end=" ")
    cur = expected
    while cur:
        print(cur.val, end=", ")
        cur = cur.next
    print()
    print()

####

    head = ListNode(0)
    head.next = ListNode(1)
    head.next.next = ListNode(2)
    m = 1
    n = 2
    expected = ListNode(1)
    expected.next = ListNode(0)
    expected.next.next = ListNode(2)

    print("m: %s, n: %s" % (m, n))
    print("argument: ", end=" ")
    cur = head
    while cur:
        print(cur.val, end=", ")
        cur = cur.next
    print()
    print("expected: ", end=" ")
    cur = expected
    while cur:
        print(cur.val, end=", ")
        cur = cur.next
    print()
    actual = Solution.reverseBetween(Solution, head, m, n)
    print("actual: ", end=" ")
    cur = expected
    while cur:
        print(cur.val, end=", ")
        cur = cur.next
    print()
    print()

####

    head = ListNode(0)
    m = 1
    n = 1
    expected = ListNode(0)

    print("m: %s, n: %s" % (m, n))
    print("argument: ", end=" ")
    cur = head
    while cur:
        print(cur.val, end=", ")
        cur = cur.next
    print()
    print("expected: ", end=" ")
    cur = expected
    while cur:
        print(cur.val, end=", ")
        cur = cur.next
    print()
    actual = Solution.reverseBetween(Solution, head, m, n)
    print("actual: ", end=" ")
    cur = expected
    while cur:
        print(cur.val, end=", ")
        cur = cur.next
    print()
    print()

