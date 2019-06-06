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
    def partition(self, head, x):
        if not head:
            return None

        small = ListNode(88)
        smallb = small
        firstbig = head
        while firstbig and firstbig.val < x:
            smallb.next = firstbig
            firstbig = firstbig.next
            smallb = smallb.next
            smallb.next = None

        if not firstbig:
            return head

        # FIRSTBIG POINTS AT THE FIRSTBIG ONE IN THE LIST
        # small holds all the small ones removed so far. It might be empty.
        # small.next tells you if you have any smalls yet.

        cur = firstbig
        while cur and cur.next:
            if cur.next.val < x:
                smallb.next = cur.next
                cur.next = cur.next.next
                smallb = smallb.next
                smallb.next = None
            else:
                cur = cur.next

        smallb.next = firstbig
        return small.next

if __name__ == '__main__':
    print("CASE")
    a = ListNode(3)
    a.next = ListNode(2)
    a.next.next = ListNode(3.5)
    a.next.next.next = ListNode(3)
    a.next.next.next.next = ListNode(.4)
    # a.next.next.next.next.next = ListNode(1)
    printl(a, "argument: ")
    actual = Solution.partition(Solution, a, 1)
    printl(actual, "actual: ")
    print(actual.val)

    print("CASE")
    a = ListNode(3)
    a.next = ListNode(2)
    a.next.next = ListNode(3.5)
    a.next.next.next = ListNode(3)
    a.next.next.next.next = ListNode(.4)
    a.next.next.next.next.next = ListNode(8)
    # a.next.next.next.next.next = ListNode(1)
    printl(a, "argument: ")
    actual = Solution.partition(Solution, a, 1)
    printl(actual, "actual: ")
    print(actual.val)

    print("CASE")
    a = ListNode(3.1)
    a.next = ListNode(2)
    a.next.next = ListNode(3.5)
    a.next.next.next = ListNode(3)
    a.next.next.next.next = ListNode(.4)
    a.next.next.next.next.next = ListNode(8)
    printl(a, "argument: ")
    actual = Solution.partition(Solution, a, 3)
    printl(actual, "actual: ")
    print(actual.val)

    print("CASE")
    a = ListNode(3.1)
    printl(a, "argument: ")
    actual = Solution.partition(Solution, a, 3)
    printl(actual, "actual: ")
    print(actual.val)

    print("CASE")
    a = ListNode(3.1)
    printl(a, "argument: ")
    actual = Solution.partition(Solution, a, 3.2)
    printl(actual, "actual: ")
    print(actual.val)



