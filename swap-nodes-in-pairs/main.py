# Definition for singly-linked list.
def printl(l):
    cur = l
    print("list: ", end=": ")
    while cur:
        print(cur.val, end=", ")
        cur = cur.next
    print()


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return None
        if head and not head.next:
            return head

        ans = ListNode(99)
        ansb = ans
        one = head
        two = head.next
        rest = two.next

        while one and two:
            ansb.next = two
            ansb = ansb.next
            if rest:
                two = rest.next
            else:
                two = None

            ansb.next = one
            ansb = ansb.next
            ansb.next = None

            one = rest
            if two:
                rest = two.next
            else:
                rest = None

        if one:
            ansb.next = one
            ansb = ansb.next

        return ans.next


if __name__ == '__main__':
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    a.next.next.next.next = ListNode(5)
    printl(a)

    actual = Solution.swapPairs(Solution, a)
    printl(actual)
    print()

    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    printl(a)

    actual = Solution.swapPairs(Solution, a)
    printl(actual)
    print()

    a = ListNode(1)
    a.next = ListNode(2)
    printl(a)

    actual = Solution.swapPairs(Solution, a)
    printl(actual)
    print()


    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    a.next.next.next.next = ListNode(5)
    a.next.next.next.next.next = ListNode(6)

    printl(a)

    actual = Solution.swapPairs(Solution, a)
    printl(actual)
    print()

