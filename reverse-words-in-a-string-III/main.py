class Solution(object):
    def reverseWords(self, s):

        words = s.split(" ")

        return " ".join([w[::-1] for w in words])


if __name__ == '__main__':
    s = "that day"
    desired = "taht yad"
    actual = Solution.reverseWords(Solution, s)
    print("arguments: %s" % s)
    print("desired : " + str(desired))
    print("actual  : " + str(actual))
    print()

    s = "that day was hot."
    desired = "taht yad saw .toh"
    actual = Solution.reverseWords(Solution, s)
    print("arguments: %s" % s)
    print("desired : " + str(desired))
    print("actual  : " + str(actual))
    print()

