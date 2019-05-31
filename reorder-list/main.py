# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        if not head.next:
            return head

        cur = head
        second = cur
        while cur and cur.next and cur.next.next and second.next.next:
            second = second.next

        while cur and cur.next and cur.next.next:
            last = second.next
            last.next = cur.next
            cur.next = last
            second.next = None

            cur = cur.next.next
            second = cur
            while cur.next and second.next.next is not None:
                second = second.next




if __name__ == '__main__':
    arg = ListNode(0)
    arg.next = ListNode(1)
    arg.next.next = ListNode(2)
    arg.next.next.next = ListNode(3)
    arg.next.next.next.next = ListNode(4)
    arg.next.next.next.next.next = ListNode(5)

    expected = ListNode(0)
    expected.next = ListNode(5)
    expected.next.next = ListNode(1)
    expected.next.next.next = ListNode(4)
    expected.next.next.next.next = ListNode(2)
    expected.next.next.next.next.next = ListNode(3)

    print("arg     : ", end=' ')
    cur = arg
    while cur:
        print(cur.val, end=', ')
        cur = cur.next
    print()

    print("expected: ", end=' ')
    cur = expected
    while cur:
        print(cur.val, end=', ')
        cur = cur.next
    print()

    Solution.reorderList(Solution, arg)

    print("actual  : ", end=' ')
    cur = arg
    while cur:
        print(cur.val, end=', ')
        cur = cur.next
    print()
    print()

    arg = ListNode(0)
    arg.next = ListNode(1)
    arg.next.next = ListNode(2)
    arg.next.next.next = ListNode(3)
    arg.next.next.next.next = ListNode(4)
    arg.next.next.next.next.next = ListNode(5)
    arg.next.next.next.next.next.next = ListNode(6)


    expected = ListNode(0)
    expected.next = ListNode(6)
    expected.next.next = ListNode(1)
    expected.next.next.next = ListNode(5)
    expected.next.next.next.next = ListNode(2)
    expected.next.next.next.next.next = ListNode(4)
    expected.next.next.next.next.next.next = ListNode(3)

    print("arg     : ", end=' ')
    cur = arg
    while cur:
        print(cur.val, end=', ')
        cur = cur.next
    print()

    print("expected: ", end=' ')
    cur = expected
    while cur:
        print(cur.val, end=', ')
        cur = cur.next
    print()

    Solution.reorderList(Solution, arg)

    print("actual  : ", end=' ')
    cur = arg
    while cur:
        print(cur.val, end=', ')
        cur = cur.next
    print()
    print()

    arg = ListNode(0)
    arg.next = ListNode(1)

    expected = ListNode(0)
    expected.next = ListNode(1)

    print("arg     : ", end=' ')
    cur = arg
    while cur:
        print(cur.val, end=', ')
        cur = cur.next
    print()

    print("expected: ", end=' ')
    cur = expected
    while cur:
        print(cur.val, end=', ')
        cur = cur.next
    print()

    Solution.reorderList(Solution, arg)

    print("actual  : ", end=' ')
    cur = arg
    while cur:
        print(cur.val, end=', ')
        cur = cur.next
    print()
    print()

    arg = ListNode(0)
    arg.next = ListNode(1)
    arg.next.next = ListNode(2)

    expected = ListNode(0)
    expected.next = ListNode(2)
    expected.next.next = ListNode(1)

    print("arg     : ", end=' ')
    cur = arg
    while cur:
        print(cur.val, end=', ')
        cur = cur.next
    print()

    print("expected: ", end=' ')
    cur = expected
    while cur:
        print(cur.val, end=', ')
        cur = cur.next
    print()

    Solution.reorderList(Solution, arg)

    print("actual  : ", end=' ')
    cur = arg
    while cur:
        print(cur.val, end=', ')
        cur = cur.next
    print()
    print()
