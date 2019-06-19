# Definition for singly-linked list.
def printl(l1, label):
    print(label + ": ", end=" ")
    cur = l1
    while cur:
        print(cur.val, end=", ")
        cur = cur.next
    print()

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        # ensure the invarient
        new = ListNode(-1)
        ans = new
        if not l1:
            return l2
        if not l2:
            return l1

        # process the body
        while l1 and l2:
            if l1.val <= l2.val:
                new.next = l1 # restructure the lists
                l1 = l1.next
            else:
                new.next = l2 # restructure the lists
                l2 = l2.next # reassign reference

            new = new.next
            new.next = None # restructure the lists

        if l1:
            new.next = l1

        if l2:
            new.next = l2

        return ans.next


if __name__ == '__main__':
    l1 = ListNode(0)
    l1.next = ListNode(1)
    l1.next.next = ListNode(2)
    l1.next.next.next = ListNode(3)
    l1.next.next.next.next = ListNode(4)
    l1.next.next.next.next.next = ListNode(5)
    l1.next.next.next.next.next.next = ListNode(6)

    l2 = ListNode(10)
    l2.next = ListNode(11)
    l2.next.next = ListNode(14)
    l2.next.next.next = ListNode(15)
    l2.next.next.next.next = ListNode(17)
    l2.next.next.next.next.next = ListNode(18)
    l2.next.next.next.next.next.next = ListNode(20)

    printl(l1, "l1")
    printl(l2, "l2")
    actual = Solution.mergeTwoLists(Solution, l1, l2)
    printl(actual, "actual")
    print()

    ##

    l1 = ListNode(0)
    l1.next = ListNode(1)
    l1.next.next = ListNode(2)
    l1.next.next.next = ListNode(3)
    l1.next.next.next.next = ListNode(4)
    l1.next.next.next.next.next = ListNode(5)
    l1.next.next.next.next.next.next = ListNode(6)

    l2 = ListNode(0)
    l2.next = ListNode(1)
    l2.next.next = ListNode(2)
    l2.next.next.next = ListNode(3)
    l2.next.next.next.next = ListNode(4)
    l2.next.next.next.next.next = ListNode(5)
    l2.next.next.next.next.next.next = ListNode(6)

    l3 = ListNode(10)
    l3.next = ListNode(11)
    l3.next.next = ListNode(12)
    l3.next.next.next = ListNode(13)
    l3.next.next.next.next = ListNode(14)
    l3.next.next.next.next.next = ListNode(15)
    l3.next.next.next.next.next.next = ListNode(16)
    l1.next.next.next.next.next.next.next = l3

    printl(l1, "l1")
    printl(l2, "l2")
    actual = Solution.mergeTwoLists(Solution, l1, l2)
    printl(actual, "actual")
    print()
