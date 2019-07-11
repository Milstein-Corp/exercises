class Solution(object):

    def lengthOfLongestSubstring_messy(self, s):
        max_length = 0
        start = 0
        index = {}

        for i, c in enumerate(s):
            if c not in index:
                max_length = max(max_length, i - start + 1)
            else:
                if start <= index[c]:
                    start = index[c]+1
                max_length = max(max_length, i - start + 1)

            index[c] = i

        return max_length


    def lengthOfLongestSubstring(self, s):
        max_length = 0
        start = 0
        index = {}

        for i, c in enumerate(s):
            if c in index and start <= index[c]:
                start = index[c] + 1
            max_length = max(max_length, i - start + 1)
            index[c] = i

        return max_length

if __name__ == '__main__':
    s = "aabcddd"
    desired = 4
    actual = Solution.lengthOfLongestSubstring(Solution, s)
    print()
    print("argument : %s" % s)
    print("desired  : " + str(desired))
    print("actual   : " + str(actual))
    print()

    s = "aaaaabbbbbccccd"
    desired = 2
    actual = Solution.lengthOfLongestSubstring(Solution, s)
    print()
    print("argument : %s" % s)
    print("desired  : " + str(desired))
    print("actual   : " + str(actual))
    print()

    s = "qwertyuiop"
    desired = 10
    actual = Solution.lengthOfLongestSubstring(Solution, s)
    print()
    print("argument : %s" % s)
    print("desired  : " + str(desired))
    print("actual   : " + str(actual))
    print()

    s = "qwertyuiopasdfghjkl"
    desired = 19
    actual = Solution.lengthOfLongestSubstring(Solution, s)
    print()
    print("argument : %s" % s)
    print("desired  : " + str(desired))
    print("actual   : " + str(actual))
    print()

    s = "qwertuuuyuiop"
    desired = 6
    actual = Solution.lengthOfLongestSubstring(Solution, s)
    print()
    print("argument : %s" % s)
    print("desired  : " + str(desired))
    print("actual   : " + str(actual))
    print()

    s = "qwerttyuiop"
    desired = 6
    actual = Solution.lengthOfLongestSubstring(Solution, s)
    print()
    print("argument : %s" % s)
    print("desired  : " + str(desired))
    print("actual   : " + str(actual))
    print()
