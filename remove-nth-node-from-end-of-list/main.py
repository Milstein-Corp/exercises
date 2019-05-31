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
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return None
        if n < 1:
            return head

        end = head
        endi = 1
        while endi != n + 1:
            endi += 1
            end = end.next
            if end is None and endi > n:
                return head.next

        remove = head

        while end.next:
            end = end.next
            remove = remove.next

        remove.next = remove.next.next

        return head


if __name__ == '__main__':
    a = None
    n = 0
    print("n: %s" % n)
    printl(a)
    actual = Solution.removeNthFromEnd(Solution, a, n)
    printl(actual)
    print()

    a = ListNode(1)
    a.next = ListNode(2)
    n = 1
    print("n: %s" % n)
    printl(a)
    actual = Solution.removeNthFromEnd(Solution, a, n)
    printl(actual)
    print()

    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    a.next.next.next.next = ListNode(5)
    n = 2
    print("n: %s" % n)
    printl(a)
    actual = Solution.removeNthFromEnd(Solution, a, n)
    printl(actual)
    print()


    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    n = 2
    printl(a)

    actual = Solution.removeNthFromEnd(Solution, a, n)
    printl(actual)
    print()

    a = ListNode(1)
    n = 1
    printl(a)

    actual = Solution.removeNthFromEnd(Solution, a, n)
    printl(actual)
    print()


    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    a.next.next.next.next = ListNode(5)
    a.next.next.next.next.next = ListNode(6)
    n = 6
    printl(a)

    actual = Solution.removeNthFromEnd(Solution, a, n)
    printl(actual)
    print()

#