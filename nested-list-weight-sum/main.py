class Solution(object):
    def depthSum(self, nestedList):

        total = Solution.sumed(Solution, nestedList, 1)
        return total

    def sumed(self, nestedList, depth):
        total = 0
        for i in nestedList:
            if isinstance(i, (list,)):
                total += Solution.sumed(Solution, i, depth + 1)
            else:
                total += i*depth
        return total




if __name__ == '__main__':
    input = [0, 1, 2, 3, [4]]
    actual = Solution.depthSum(Solution, input)
    desired = input
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()
