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
            newpath = nums[i] + max(pp, ppp)
            ppp = pp
            pp = p
            p = newpath
            i += 1

        return max(pp, p)

if __name__ == '__main__':
    ins = [5, 3, 7, 1, 8]
    desired = 20
    actual = Solution.rob(Solution, ins)
    print("input %s" % ins)
    print("desired %s" % desired)
    print("actual %s" % actual)
    print()

    ins = [5, 3, 7, 1, 8, 4]
    desired = 20
    actual = Solution.rob(Solution, ins)
    print("input %s" % ins)
    print("desired %s" % desired)
    print("actual %s" % actual)
    print()

    ins = [5, 3, 7, 1, 8, 4, 10]
    desired = 30
    actual = Solution.rob(Solution, ins)
    print("input %s" % ins)
    print("desired %s" % desired)
    print("actual %s" % actual)
    print()

    ins = [5, 3, 7, 1, 8, 4, 10, 1]
    desired = 30
    actual = Solution.rob(Solution, ins)
    print("input %s" % ins)
    print("desired %s" % desired)
    print("actual %s" % actual)
    print()

    ins = [5, 3, 7, 1, 8, 4, 10, 11]
    desired = 31
    actual = Solution.rob(Solution, ins)
    print("input %s" % ins)
    print("desired %s" % desired)
    print("actual %s" % actual)
    print()

    ins = [5, 4, 5]
    desired = 10
    actual = Solution.rob(Solution, ins)
    print("input %s" % ins)
    print("desired %s" % desired)
    print("actual %s" % actual)
    print()

