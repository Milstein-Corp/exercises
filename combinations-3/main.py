class Solution(object):
    def combine(self, n, k):
        ans = []
        recent = list(range(n - k + 1, n + 1))
        ans.append(list.copy(recent))
        i = 0

        while i != k:
            temp = recent[i] - 1
            if 0 < temp and temp not in recent:
                recent[i] = temp
                for j in range(i - 1, -1, -1):
                    recent[j] = recent[j + 1] - 1
                    print(recent)
                ans.append(list.copy(recent))
                i = 0
            else:
                i += 1

        return ans


if __name__ == '__main__':
    n = 3
    k = 2
    actual = Solution.combine(Solution, n, k)
    desired = [[2, 3], [1, 3], [1, 2]]
    print("actual: %s" % actual)
    print("desired: %s" % desired)

    n = 4
    k = 2
    actual = Solution.combine(Solution, n, k)
    desired = [[3, 4], [2, 4], [1, 4], [2, 3], [1, 3], [1, 2]]
    print("actual: %s" % actual)
    print("desired: %s" % desired)
