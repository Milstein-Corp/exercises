import queue


class node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def verticalTraversal(self, root):
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            curr = q.get()
            print(curr.val)
            if curr.left:
                q.put(curr.left)
            if curr.right:
                q.put(curr.right)


if __name__ == '__main__':
    a = node(1)
    b = node(2)
    c = node(3)
    d = node(4)
    e = node(5)
    f = node(6)
    g = node(7)
    h = node(8)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    d.left = h

    Solution.verticalTraversal(Solution, a)
