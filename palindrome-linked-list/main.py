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
    def isPalindrome(self, head):
        end = head
        rest = head
        n = 0
        rev = None

        while end and end.next:
            end = end.next.next  # 1 + 2n
            rest.next, rev, rest = rev, rest, rest.next  # 1 + n
            n += 1

        middle = rest
        if end:
            rest = rest.next

        isPal = True
        while rev and rest:
            if rev.val != rest.val:
                isPal = False
            rev.next, rev, middle = middle, rev.next, rev
            rest = rest.next


        return isPal


if __name__ == '__main__':
    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(3)
    a.next.next.next.next = ListNode(2)
    a.next.next.next.next.next = ListNode(1)
    printl(a, "argument: ")
    actual = Solution.isPalindrome(Solution, a)
    printl(a, "argument: ")
    print(actual)
    print()

    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(3)
    a.next.next.next.next = ListNode(2)
    a.next.next.next.next.next = ListNode(8)
    printl(a, "argument: ")
    actual = Solution.isPalindrome(Solution, a)
    printl(a, "argument: ")
    print(actual)
    print()

    a = ListNode(2)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(2)
    a.next.next.next.next = ListNode(2)
    printl(a, "argument: ")
    actual = Solution.isPalindrome(Solution, a)
    printl(a, "argument: ")
    print(actual)
    print()

    a = ListNode(1)
    a.next = ListNode(2)
    a.next.next = ListNode(3)
    a.next.next.next = ListNode(2)
    a.next.next.next.next = ListNode(1)
    printl(a, "argument: ")
    actual = Solution.isPalindrome(Solution, a)
    printl(a, "argument: ")
    print(actual)
    print()

    a = ListNode(1)
    a.next = ListNode(1)
    printl(a, "argument: ")
    actual = Solution.isPalindrome(Solution, a)
    printl(a, "argument: ")
    print(actual)
    print()

    a = ListNode(1)
    a.next = ListNode(9)
    printl(a, "argument: ")
    actual = Solution.isPalindrome(Solution, a)
    printl(a, "argument: ")
    print(actual)
    print()

    a = ListNode(1)
    printl(a, "argument: ")
    actual = Solution.isPalindrome(Solution, a)
    printl(a, "argument: ")
    print(actual)
    print()
