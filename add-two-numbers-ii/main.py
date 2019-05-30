# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = []
        c = l1
        while c:
            n1.append(c.val)
            c = c.next

        n2 = []
        c = l2
        while c:
            n2.append(c.val)
            c = c.next

        ans = 0
        place = 0
        while n2:
            ans += 10**place * n2.pop()
            place += 1

        place = 0
        while n1:
            ans += 10**place * n1.pop()
            place += 1

        place = 0
        num = ans / 10 ** place
        result = None

        while num > 0:
            digit = int(num % 10)
            new = ListNode(digit)
            new.next = result
            result = new

            place += 1
            num = int(ans / 10**place)

        if not result:
            return ListNode(0)

        return result


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(3)
    l1.next.next = ListNode(4)
    l1.next.next.next = ListNode(5)

    l2 = ListNode(1)
    l2.next = ListNode(2)
    l2.next.next = ListNode(3)

    expected = ListNode(2)
    expected.next = ListNode(4)
    expected.next.next = ListNode(6)
    expected.next.next.next = ListNode(8)
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
    l1.next = ListNode(9)
    l1.next.next = ListNode(4)
    l1.next.next.next = ListNode(5)

    l2 = ListNode(1)
    l2.next = ListNode(2)
    l2.next.next = ListNode(3)

    expected = ListNode(3)
    expected.next = ListNode(0)
    expected.next.next = ListNode(6)
    expected.next.next.next = ListNode(8)
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
