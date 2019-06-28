class Solution(object):
    def firstUniqChar(self, s):
        d = {}

        for c in s:
            try:
                d[c] = d[c] + 1
            except KeyError:
                d[c] = 1
            print(d)

        counts = list(d.items())
        print(counts)

        counts.sort(key=lambda x: x[1])

        print(counts)
        if counts[0][1] == 1:

            return s.find(counts[0][0])
        else:
            return -1


if __name__ == '__main__':
    # s = "aaaaabc"
    # desired = 5
    # actual = Solution.firstUniqChar(Solution, s)
    # print("arguments: %s" % s)
    # print("desired : " + str(desired))
    # print("actual  : " + str(actual))
    # assert desired == actual
    # print()
    #
    # s = "aaaaacb"
    # desired = 5
    # actual = Solution.firstUniqChar(Solution, s)
    # print("arguments: %s" % s)
    # print("desired : " + str(desired))
    # print("actual  : " + str(actual))
    # assert desired == actual
    # print()
    #
    # s = "aaaaaccbb"
    # desired = -1
    # actual = Solution.firstUniqChar(Solution, s)
    # print("arguments: %s" % s)
    # print("desired : " + str(desired))
    # print("actual  : " + str(actual))
    # assert desired == actual
    # print()

    # s = "aaauaaccbb"
    # desired = 3
    # actual = Solution.firstUniqChar(Solution, s)
    # print("arguments: %s" % s)
    # print("desired : " + str(desired))
    # print("actual  : " + str(actual))
    # assert desired == actual
    # print()

    s = "leetcode"
    desired = 0
    actual = Solution.firstUniqChar(Solution, s)
    print("arguments: %s" % s)
    print("desired : " + str(desired))
    print("actual  : " + str(actual))
    assert desired == actual
    print()
