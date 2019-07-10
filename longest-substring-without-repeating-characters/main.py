class Solution(object):

    def lengthOfLongestSubstring(self, s):
        used = {}
        max_length = start = 0
        for i, c in enumerate(s):
            print("i, c : %s, %s" % (i,c))
            print(used)
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                max_length = max(max_length, i - start + 1)
            print("i, c : %s, %s" % (i,c))
            print(used)
            print()
            print()
            used[c] = i

        return max_length

if __name__ == '__main__':
    s = "ellhellhell"
    desired = 3

    actual = Solution.lengthOfLongestSubstring(Solution, s)
    print()
    print("argument : %s" % s)
    print("desired  : " + str(desired))
    print("actual   : " + str(actual))
    print()
