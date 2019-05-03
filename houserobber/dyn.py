class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])

        ai = 0
        a = nums[0]
        bi = 1
        b = nums[1]
        ci = 2
        c = nums[2] + nums[0]

        for i in range(len(nums)-3):
            k = i + 3
            best = nums[k] + max(a, b)
            a = b
            b = c
            c = best
            # c now holds the best value for index k
            # b holds the best value for k-1
            # a holds the best value for k-2

        return max(c, b)



def main():
    # Solution.rob(Solution, 5)

    # input = [4, 5]
    # output = 5
    # a = Solution.rob(Solution, input)
    # print("desired output: %d" % output)
    # print("actual output: %d" % a)
    # print()

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

