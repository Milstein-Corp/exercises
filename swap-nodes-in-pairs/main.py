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

        p0 = ListNode(99)
        ans = p0
        ans.next = head

        while p0.next and p0.next.next:
            p1, p2 = p0.next, p0.next.next  # (p0.next).next = (p1).next
            # these references are set for the duration of the while loop
            p1.next = p2.next
            p0.next = p2
            p2.next = p1
            p0 = p0.next.next

        return ans.next



if __name__ == '__main__':
    a = None
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
    printl(a)

    actual = Solution.swapPairs(Solution, a)
    printl(actual)
    print()
    #
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    printl(a)

    actual = Solution.swapPairs(Solution, a)
    printl(actual)
    print()

    a = ListNode(1)
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
#
#