class Solution(object):
    def combine(self, n, k):
        if k > n:
            return []

        ans = []
        recent = list(range(n-k+1, n+1))

        if recent:
            ans.append(list.copy(recent))

        i = 0

        while i < k:
            if i == 0:
                bound = 0
            else:
                bound = recent[i-1]
            if bound < recent[i] - 1:
                recent[i] = recent[i] - 1
                for j in range(i, 0, -1):
                    recent[j-1] = recent[j] - 1
                ans.append(list.copy(recent))
                i = 0
            else:
                i += 1

        return ans





if __name__ == '__main__':
    actual = Solution.combine(Solution, 2, 2)
    desired = [[1, 2]]
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    actual = Solution.combine(Solution, 3, 2)
    desired = [[2, 3], [1, 3], [1, 2]]
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    actual = Solution.combine(Solution, 4, 2)
    desired = [[3, 4], [2, 4], [1, 4], [2, 3], [1, 3], [1, 2]]
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    actual = Solution.combine(Solution, 1, 1)
    desired = [[1]]
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    actual = Solution.combine(Solution, 1, 0)
    desired = []
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    actual = Solution.combine(Solution, 0, 0)
    desired = []
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()
