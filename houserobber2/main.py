class Solution(object):
    def rob(self, nums):
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        ppp = nums[0]
        pp = nums[1]
        p = nums[2] + nums[0]
        i = 3

        while i < len(nums):
            # invariant: the best path ending at i is unknown.
            bestp = max(ppp, pp)
            best = bestp + nums[i]  # I discovered the best path ending at i
            # break the invariant, advancing to new data
            i += 1
            # restore part of the invariant
            ppp = pp
            pp = p
            p = best

        return max(p, pp)


if __name__ == '__main__':
    input = [1, 2, 3, 1]
    actual = Solution.rob(Solution, input)
    desired = 4
    print("actual: %s" % actual)
    print("desired: %s" % desired)
    print()

    input = [1, 2, 3, 1, 5, 1, 6]
    actual = Solution.rob(Solution, input)
    desired = 15
    print("actual: %s" % actual)
    print("desired: %s" % desired)
    print()

    input = [1, 2, 3, 5, 1, 1, 6]
    actual = Solution.rob(Solution, input)
    desired = 13
    print("actual: %s" % actual)
    print("desired: %s" % desired)
    print()

    input = [1, 2, 10, 5, 1, 1, 6]
    actual = Solution.rob(Solution, input)
    desired = 18
    print("actual: %s" % actual)
    print("desired: %s" % desired)
    print()

    input = [1, 2, 10, 15, 1, 6, 6]
    actual = Solution.rob(Solution, input)
    desired = 23
    print("actual: %s" % actual)
    print("desired: %s" % desired)
    print()

    input = [1, 2, 10, 15, 1, 7, 6]
    actual = Solution.rob(Solution, input)
    desired = 24
    print("actual: %s" % actual)
    print("desired: %s" % desired)
    print()


