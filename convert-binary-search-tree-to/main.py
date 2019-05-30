
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def treeToDoublyList(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        s = []
        cur = root

        s.append(root.left)

        while s:
            lee = s.pop()
            if lee.left:
                s.append(lee)
                s.append(lee.left)
            else 


            if cur.left:
                s.append(cur)
                cur = cur.left
            else:
                print(cur.val)
                cur = cur.right
                s.append(cur.right)



            s.append(cur)
            while cur.left:
                s.append(cur.left)
                cur = cur.left

            while s:
                cur = s.pop()
                print(cur.val)

            if cur.right:
                s.append(cur.right)



if __name__ == '__main__':
    l21 = Node(1, None, None)
    l22 = Node(3, None, None)
    l23 = Node(5, None, None)
    l24 = None

    n11 = Node(2, l21, l22)
    n12 = Node(6, l23, l24)
    n01 = Node(4, n11, n12)

    actual = Solution.treeToDoublyList(Solution, n01)



