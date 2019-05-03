class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        elif len(nums) == 3:
            return max(nums[0] + nums[2], nums[1])
        else:
            c1 = nums[0]
            c2 = nums[1]
            r1 = nums[2:]
            r2 = nums[3:]
            return max(c1 + Solution.rob(Solution, r1), c2 + Solution.rob(Solution, r2))


def main():
    # Solution.rob(Solution, 5)

    input = [4, 5]
    output = 5
    a = Solution.rob(Solution, input)
    print("desired output: %d" % output)
    print("actual output: %d" % a)
    print()

    input = [4, 5, 6]
    output = 10
    a = Solution.rob(Solution, input)
    print("desired output: %d" % output)
    print("actual output: %d" % a)
    print()

    input = [11, 5, 12, 11]
    output = 23
    a = Solution.rob(Solution, input)
    print("desired output: %d" % output)
    print("actual output: %d" % a)
    print()

    input = [11, 5, 10, 11]
    output = 22
    a = Solution.rob(Solution, input)
    print("desired output: %d" % output)
    print("actual output: %d" % a)
    print()

    input = [1, 11, 12, 11]
    output = 22
    a = Solution.rob(Solution, input)
    print("desired output: %d" % output)
    print("actual output: %d" % a)
    print()

    input = [11, 1, 1, 11, 12, 11]
    output = 33
    a = Solution.rob(Solution, input)
    print("desired output: %d" % output)
    print("actual output: %d" % a)
    print()

if __name__ == '__main__':
    main()

