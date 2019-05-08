class Solution(object):
    def combine(self, n, k):
        if k > n:
            return []

        ref = list(range(1, n + 1))
        ans = []
        curr = ref[n-k:n]
        ans.append(list.copy(curr))
        i = 0

        while i != k:
            temp = curr[i] - 1
            if temp > 0 and temp not in curr:
                curr[i] = temp
                for j in range(i-1, -1, -1):
                    curr[j] = curr[j+1] - 1
                ans.append(list.copy(curr))
                # reset [0, i)
                i = 0
            else:
                i += 1


        return sorted(ans)


if __name__ == '__main__':


    n = 4
    k = 3
    actual = Solution.combinations(Solution, n, k)
    desired = sorted([[2, 3, 4], [1, 3, 4], [1, 2, 4], [1, 2, 3]])
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    n = 4
    k = 2
    actual = Solution.combinations(Solution, n, k)
    desired = sorted([[2, 4], [3, 4], [2, 3], [1, 2], [1, 3], [1, 4]])
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    n = 3
    k = 3
    actual = Solution.combinations(Solution, n, k)
    desired = [[1, 2, 3]]
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    n = 4
    k = 7
    actual = Solution.combinations(Solution, n, k)
    desired = []
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()


