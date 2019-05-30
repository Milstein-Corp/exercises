# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        ans = ListNode(0)
        p1 = l1
        p2 = l2
        p3 = ans
        carry = 0

        while p1 and p2:
            res = p1.val + p2.val + carry
            carry = int(res / 10)
            res = res % 10
            p3.next = ListNode(res)
            p1 = p1.next
            p2 = p2.next
            p3 = p3.next

        while p1:
            res = p1.val + carry
            carry = int(res / 10)
            res = res % 10
            p3.next = ListNode(res)
            p1 = p1.next
            p3 = p3.next

        while p2:
            res = p2.val + carry
            carry = int(res / 10)
            res = res % 10
            p3.next = ListNode(res)
            p2 = p2.next
            p3 = p3.next

        if carry != 0:
            p3.next = ListNode(1)

        return ans.next



if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(3)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(2)
    l2.next.next = ListNode(3)

    expected = ListNode(3)
    expected.next = ListNode(5)
    expected.next.next = ListNode(7)
    actual = Solution.addTwoNumbers(Solution, l1, l2)

    cur = l1
    print("l1: ", end="")
    while cur:
        print(cur.val, end=", ")
        cur = cur.next
    print()

    cur = l2
    print("l2: ", end="")
    while cur:
        print(cur.val, end=", ")
        cur = cur.next
    print()

    cur = expected
    print("expected: ", end="")
    while cur:
        print(cur.val, end=", ")
        cur = cur.next
    print()

    cur = actual
    print("actual: ", end="")
    while cur:
        print(cur.val, end=", ")
        cur = cur.next
    print()

    print()

    l1 = ListNode(9)
    l1.next = ListNode(3)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(2)
    l2.next.next = ListNode(3)

    expected = ListNode(0)
    expected.next = ListNode(6)
    expected.next.next = ListNode(7)
    actual = Solution.addTwoNumbers(Solution, l1, l2)

    cur = l1
    print("l1: ", end="")
    while cur:
        print(cur.val, end=", ")
        cur = cur.next
    print()

    cur = l2
    print("l2: ", end="")
    while cur:
        print(cur.val, end=", ")
        cur = cur.next
    print()

    cur = expected
    print("expected: ", end="")
    while cur:
        print(cur.val, end=", ")
        cur = cur.next
    print()

    cur = actual
    print("actual: ", end="")
    while cur:
        print(cur.val, end=", ")
        cur = cur.next
    print()
    print()

    l1 = ListNode(2)
    l1.next = ListNode(3)

    l2 = ListNode(1)
    l2.next = ListNode(2)
    l2.next.next = ListNode(3)

    expected = ListNode(3)
    expected.next = ListNode(5)
    expected.next.next = ListNode(3)
    actual = Solution.addTwoNumbers(Solution, l1, l2)

    cur = l1
    print("l1: ", end="")
    while cur:
        print(cur.val, end=", ")
        cur = cur.next
    print()

    cur = l2
    print("l2: ", end="")
    while cur:
        print(cur.val, end=", ")
        cur = cur.next
    print()

    cur = expected
    print("expected: ", end="")
    while cur:
        print(cur.val, end=", ")
        cur = cur.next
    print()

    cur = actual
    print("actual: ", end="")
    while cur:
        print(cur.val, end=", ")
        cur = cur.next
    print()
    print()

    l1 = ListNode(9)
    l1.next = ListNode(9)

    l2 = ListNode(4)
    l2.next = ListNode(6)
    l2.next.next = ListNode(8)

    expected = ListNode(3)
    expected.next = ListNode(6)
    expected.next.next = ListNode(9)
    actual = Solution.addTwoNumbers(Solution, l1, l2)

    cur = l1
    print("l1: ", end="")
    while cur:
        print(cur.val, end=", ")
        cur = cur.next
    print()

    cur = l2
    print("l2: ", end="")
    while cur:
        print(cur.val, end=", ")
        cur = cur.next
    print()

    cur = expected
    print("expected: ", end="")
    while cur:
        print(cur.val, end=", ")
        cur = cur.next
    print()

    cur = actual
    print("actual: ", end="")
    while cur:
        print(cur.val, end=", ")
        cur = cur.next
    print()
    print()





