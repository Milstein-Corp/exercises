class Solution(object):
    def rob(self, input):
        if len(input) == 0:
            return 0
        elif len(input) == 1:
            return input[1]
        elif len(input) == 2:
            return max(input[0], input[1])
        elif len(input) == 3:
            return max(input[0]+input[2], input[1])

        a = input[0]
        b = input[1]
        c = input[2] + input[0]
        i = 3

        while i != len(input):
            best = max(a, b)
            a = b
            b = c
            c = best + input[i]
            i += 1

        return max(b, c)


if __name__ == '__main__':
    input = [1, 3, 4, 8]
    actual = Solution.rob(Solution, input)
    desired = 11
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    input = [10, 3, 10, 8, 10]
    actual = Solution.rob(Solution, input)
    desired = 30
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    input = [1, 3, 4, 8, 10]
    actual = Solution.rob(Solution, input)
    desired = 15
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    input = [1, 3, 4, 8, 2]
    actual = Solution.rob(Solution, input)
    desired = 11
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()
