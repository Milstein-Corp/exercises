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

        one = ListNode(99)
        two = ListNode(99)
        oneb = one
        twob = two
        curr1 = head
        curr2 = head.next

        while curr1 and curr2:
            oneb.next = curr1
            twob.next = curr2
            oneb = oneb.next
            twob = twob.next
            curr1 = curr1.next.next
            if curr1:
                curr2 = curr1.next
            else:
                curr2 = None
            oneb.next = None
            twob.next = None

        if curr1:
            oneb.next = curr1
            curr1 = None
            oneb = oneb.next

        one = one.next
        two = two.next
        two = Solution.reverse(Solution, two)
        # lists are splintered
        print("one     : ", end=' ')
        cur = one
        while cur:
            print(cur.val, end=', ')
            cur = cur.next
        print()

        print("two     : ", end=' ')
        cur = two
        while cur:
            print(cur.val, end=', ')
            cur = cur.next
        print()



        cur = one
        while cur and two:
            insert = two
            two = two.next

            insert.next = cur.next
            cur.next = insert
            cur = cur.next.next


        return one


    def reverse(self, head):
        growing = None
        move = None
        rest = head

        while rest:
            move = rest
            rest = rest.next

            move.next = growing
            growing = move

        return growing






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

    act = Solution.reorderList(Solution, arg)

    print("actual  : ", end=' ')
    cur = act
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

    act = Solution.reorderList(Solution, arg)

    print("actual  : ", end=' ')
    cur = act
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

    act = Solution.reorderList(Solution, arg)

    print("actual  : ", end=' ')
    cur = act
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

    act = Solution.reorderList(Solution, arg)

    print("actual  : ", end=' ')
    cur = act
    while cur:
        print(cur.val, end=', ')
        cur = cur.next
    print()
    print()

    arg = ListNode(0)

    expected = ListNode(0)

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

    act = Solution.reorderList(Solution, arg)

    print("actual  : ", end=' ')
    cur = act
    while cur:
        print(cur.val, end=', ')
        cur = cur.next
    print()
    print()

    arg = ListNode(1)
    arg.next = ListNode(2)
    arg.next.next = ListNode(3)
    arg.next.next.next = ListNode(4)

    expected = ListNode(1)
    expected.next = ListNode(4)
    expected.next.next = ListNode(2)
    expected.next.next.next = ListNode(3)

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

    act = Solution.reorderList(Solution, arg)

    print("actual  : ", end=' ')
    cur = act
    while cur:
        print(cur.val, end=', ')
        cur = cur.next
    print()
    print()
