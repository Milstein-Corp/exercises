# Definition for singly-linked list.
def printl(l):
    cur = l
    print("list: ", end=": ")
    print(cur.val, end=", ")
    cur = cur.next
    while cur != l:
        print(cur.val, end=", ")
        cur = cur.next
    print(cur.val, end=", ")
    print()


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def insert(self, head, insertVal):
        if not head:
            ans = ListNode(insertVal)
            ans.next = ans
            return ans
        if head is head.next:
            head.next = ListNode(insertVal)
            head.next.next = head
            return head

        allsame = True
        val = head.val
        cur = head.next

        while cur is not head:
            if cur.val != val:
                allsame = False
            cur = cur.next

        if allsame:
            cur = head.next
            head.next = ListNode(insertVal)
            head.next.next = cur
            return head

        # gotta be two
        p = head
        pp = head.next

        fit = p.val <= insertVal <= pp.val



        while not fit:
            p = p.next
            pp = pp.next
            fit = p.val <= insertVal <= pp.val
            if pp.val < p.val:
                fit = insertVal >= p.val or insertVal <= pp.val

        p.next = ListNode(insertVal)
        p.next.next = pp

        return head


if __name__ == '__main__':

    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    a.next.next.next.next = ListNode(5)
    a.next.next.next.next.next = a
    n = 2
    print("n: %s" % n)
    printl(a)
    actual = Solution.insert(Solution, a, n)
    printl(actual)
    print()

    a = ListNode(1)
    a.next = a
    n = 4
    print("n: %s" % n)
    print("list: : %s" % a.val)
    # printl(a)
    actual = Solution.insert(Solution, a, n)
    printl(actual)
    print()

    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    a.next.next.next.next = ListNode(5)
    a.next.next.next.next.next = a
    n = 0
    print("n: %s" % n)
    printl(a)
    actual = Solution.insert(Solution, a, n)
    printl(actual)
    print()

    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    a.next.next.next.next = ListNode(5)
    a.next.next.next.next.next = a
    n = 6
    print("n: %s" % n)
    printl(a)
    actual = Solution.insert(Solution, a, n)
    printl(actual)
    print()

    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(4)
    a.next.next.next.next = ListNode(5)
    a.next.next.next.next.next = a
    n = 5
    print("n: %s" % n)
    printl(a)
    actual = Solution.insert(Solution, a, n)
    printl(actual)
    print()

    a = ListNode(3)
    a.next = ListNode(4)
    a.next.next = ListNode(1)
    a.next.next.next = a
    n = 2
    print("n: %s" % n)
    printl(a)
    actual = Solution.insert(Solution, a, n)
    printl(actual)
    print()

    a = ListNode(3)
    a.next = ListNode(3)
    a.next.next = ListNode(3)
    a.next.next.next = a
    n = 0
    print("n: %s" % n)
    printl(a)
    actual = Solution.insert(Solution, a, n)
    printl(actual)
    print()

    a = None
    n = 1
    print("n: %s" % n)
    # printl(a)
    actual = Solution.insert(Solution, a, n)
    printl(actual)
    print()


    # a = ListNode(1)
    # a.next = ListNode(2)
    # a.next.next = ListNode(3)
    # n = 2
    # printl(a)
    #
    # actual = Solution.insert(Solution, a, n)
    # printl(actual)
    # print()
    #
    # a = ListNode(1)
    # n = 1
    # printl(a)
    #
    # actual = Solution.insert(Solution, a, n)
    # printl(actual)
    # print()
    #
    #
    # a = ListNode(1)
    # a.next = ListNode(2)
    # a.next.next = ListNode(3)
    # a.next.next.next = ListNode(4)
    # a.next.next.next.next = ListNode(5)
    # a.next.next.next.next.next = ListNode(6)
    # n = 6
    # printl(a)
    #
    # actual = Solution.insert(Solution, a, n)
    # printl(actual)
    # print()

#