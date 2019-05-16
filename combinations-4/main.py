class Solution(object):
    def combine(self, n, k):
        if k > n:
            return []
        if k == 0:
            return []
        if n == 0:
            return []

        recent = list(range(n-k+1, n+1))
        ans = [list.copy(recent)] # xxxxx

        i = 0

        while i < k:
            temp = recent[i] - 1
            if 0 < temp and temp not in recent:
                recent[i] = temp
                for j in range(i-1, -1, -1): #xxxxx
                    recent[j] = recent[j+1] - 1
                ans.append(list.copy(recent)) # xxxxx
                i = 0 # xxx
            else:
                i += 1
        return ans

if __name__ == '__main__':
    n = 3
    k = 2
    actual = Solution.combine(Solution, n, k)
    desired = [[2, 3], [1,3], [1, 2]]
    print()
    print("input %s %s" % (n, k))
    print("actual %s" % actual)
    print("desired %s" % desired)

    n = 1
    k = 1
    actual = Solution.combine(Solution, n, k)
    desired = [[1]]
    print()
    print("input %s %s" % (n, k))
    print("actual %s" % actual)
    print("desired %s" % desired)
