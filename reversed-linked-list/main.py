# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        a = head

        if not a:
            return None

        if not a.next:
            return a

        if not a.next.next:
            first = a
            second = a.next
            first.next = None

            second.next = first

            return second

        prev = a
        curr = a.next
        hank = a.next.next
        prev.next = None

        while hank:
            # advance
            curr.next = prev
            # restore
            prev = curr
            curr = hank
            hank = hank.next

        # hank == None
        curr.next = prev

        return curr


def print_ll(testhead):
    curr = testhead
    while curr:
        print(curr.val, end=',')
        curr = curr.next
    print()



def main():
    # Test batch one
    testhead = ListNode(1)
    testhead.next = ListNode(2)
    testhead.next.next = ListNode(3)
    testhead.next.next.next = ListNode(4)
    testhead.next.next.next.next = ListNode(5)
    print("input: ", end='')
    print_ll(testhead)
    print("output: ", end='')
    testresult = Solution.reverseList(Solution, testhead)
    print_ll(testresult)

    # Test batch two
    testhead = ListNode(10)
    testhead.next = ListNode(9)
    testhead.next.next = ListNode(8)
    testhead.next.next.next = ListNode(7)
    testhead.next.next.next.next = ListNode(6)
    testhead.next.next.next.next.next = testresult
    print("input: ", end='')
    print_ll(testhead)
    print("output: ", end='')
    testresult = Solution.reverseList(Solution, testhead)
    print_ll(testresult)

    # Test batch three
    testhead = ListNode(0)
    print("input: ", end='')
    print_ll(testhead)
    testresult = Solution.reverseList(Solution, testhead)
    print("output: ", end='')
    print_ll(testresult)

    # Test Batch Four
    testhead = None
    print("input: ", end='')
    print_ll(testhead)
    testresult = Solution.reverseList(Solution, testhead)
    print("output: ", end='')
    print_ll(testresult)


if __name__ == '__main__':
    main()
