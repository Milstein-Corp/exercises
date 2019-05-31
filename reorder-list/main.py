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
        counter = 1
        while cur.next:
            cur = cur.next
            counter += 1

        if counter % 2 == 0:  # 2k nodes
            cur = head
            index = 1
            k = int(counter / 2)
            for i in range(k - 1):
                cur = cur.next
                index += 1
            assert index == k
        else:  # 2k + 1 nodes
            cur = head
            index = 1
            k = int((counter - 1) / 2)
            for i in range(k):
                cur = cur.next
                index += 1
            assert index == k + 1

        headb = cur
        backhalf = cur.next
        headb.next = None
        # lists are splintered
        backhalf = Solution.reverse(Solution, backhalf)

        cur = head
        while cur and backhalf:
            insert = backhalf
            backhalf = backhalf.next

            insert.next = cur.next
            cur.next = insert
            cur = cur.next.next

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

    # arg = ListNode(0)
    # arg.next = ListNode(1)
    # arg.next.next = ListNode(2)
    #
    # expected = ListNode(0)
    # expected.next = ListNode(2)
    # expected.next.next = ListNode(1)
    #
    # print("arg     : ", end=' ')
    # cur = arg
    # while cur:
    #     print(cur.val, end=', ')
    #     cur = cur.next
    # print()
    #
    # print("expected: ", end=' ')
    # cur = expected
    # while cur:
    #     print(cur.val, end=', ')
    #     cur = cur.next
    # print()
    #
    # act = Solution.reorderList(Solution, arg)
    #
    # print("actual  : ", end=' ')
    # cur = act
    # while cur:
    #     print(cur.val, end=', ')
    #     cur = cur.next
    # print()
    # print()
    #
    # arg = ListNode(0)
    #
    # expected = ListNode(0)
    #
    # print("arg     : ", end=' ')
    # cur = arg
    # while cur:
    #     print(cur.val, end=', ')
    #     cur = cur.next
    # print()
    #
    # print("expected: ", end=' ')
    # cur = expected
    # while cur:
    #     print(cur.val, end=', ')
    #     cur = cur.next
    # print()
    #
    # act = Solution.reorderList(Solution, arg)
    #
    # print("actual  : ", end=' ')
    # cur = act
    # while cur:
    #     print(cur.val, end=', ')
    #     cur = cur.next
    # print()
    # print()
    #
    # arg = ListNode(1)
    # arg.next = ListNode(2)
    # arg.next.next = ListNode(3)
    # arg.next.next.next = ListNode(4)
    #
    # expected = ListNode(1)
    # expected.next = ListNode(4)
    # expected.next.next = ListNode(2)
    # expected.next.next.next = ListNode(3)
    #
    # print("arg     : ", end=' ')
    # cur = arg
    # while cur:
    #     print(cur.val, end=', ')
    #     cur = cur.next
    # print()
    #
    # print("expected: ", end=' ')
    # cur = expected
    # while cur:
    #     print(cur.val, end=', ')
    #     cur = cur.next
    # print()
    #
    # act = Solution.reorderList(Solution, arg)
    #
    # print("actual  : ", end=' ')
    # cur = act
    # while cur:
    #     print(cur.val, end=', ')
    #     cur = cur.next
    # print()
    # print()
