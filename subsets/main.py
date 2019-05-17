class Solution(object):
    def subsets(self, nums):
        n = len(nums)

        indices = []

        for k in range(0, n+1):
            for subset in Solution.combine(Solution, n, k):
                indices.append(subset)

        indices = sorted(indices)
        indices = sorted(indices, key=len)
        #
        # for subset in indices:
        #     print(subset)

        # print(indices)
        finalans = []

        for subset in indices:
            newsubset = []
            for ele in subset:
                newsubset.append(nums[ele-1])
            finalans.append(newsubset)

        print(len(finalans))
        return len(finalans)

    def combine(self, n, k):

        recent = list(range(n-k+1, n+1))
        ans = []
        ans.append(list.copy(recent))
        i = 0
        while i < k:
            temp = recent[i] - 1
            if temp > 0 and temp not in recent:
                recent[i] = temp
                for j in range(i-1, -1, -1):
                    recent[j] = recent[j+1] - 1
                ans.append(list.copy(recent))
                i = 0
            else:
                i+=1

        return ans


if __name__ == '__main__':
    # n = 4
    # k = 2
    # actual = Solution.combine(Solution, n, k)
    # desired = [[3, 4], [2, 4], [1, 4], [2, 3], [1, 3], [1, 2]]
    # print("desired: %s" % desired)
    # print("actual: %s" % actual)
    # print()
    #
    # n = 4
    # k = 1
    # actual = Solution.combine(Solution, n, k)
    # desired = [[4], [3], [2], [1]]
    # print("desired: %s" % desired)
    # print("actual: %s" % actual)
    # print()
    Solution.subsets(Solution, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
