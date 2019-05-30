# Definition for a Node.
from collections import defaultdict


class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        df = defaultdict(lambda: Node(0, None, None))
        df[None] = None
        n = head

        while n:
            df[n] = Node(n.val, None, None)
            n = n.next

        n = head

        while n:
            df[n].next = df[n.next]
            df[n].random = df[n.random]
            n = n.next


        return df[head]


if __name__ == '__main__':
    cur = Node(3, None, None)
    cur = Node(2, cur, None)
    cur = Node(1, cur, None)
    l1 = cur
    l1.random = l1.next.next
    copy = Solution.copyRandomList(Solution, l1)

    print("l1  : ", end="")
    while cur:
        print(cur.val, end=" ")
        if cur.random:
            print("(" + str(cur.random.val) + ")", end=", ")
        else:
            print("(N)", end=", ")

        cur = cur.next
    print()

    cur = copy
    print("copy: ", end="")
    while cur:
        print(cur.val, end=" ")
        if cur.random:
            print("(" + str(cur.random.val) + ")", end=", ")
        else:
            print("(N)", end=", ")

        cur = cur.next
    print()
