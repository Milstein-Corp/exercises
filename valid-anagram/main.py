class Solution(object):
    def isAnagram(self, s, t):
        # one = sorted(s)
        # two = sorted(t)

        return all([s.count(c) == t.count(c) for c in s+t])

        # return one == two



if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    actual = Solution.isAnagram(Solution, s, t)
    desired = True
    print("s, t: %s %s " % (s, t))
    print("desired : " + str(desired))
    print("actual  : " + str(actual))
    assert actual == desired
    print()

    s = "rat"
    t = "car"
    actual = Solution.isAnagram(Solution, s, t)
    desired = False
    print("s, t: %s %s " % (s, t))
    print("desired : " + str(desired))
    print("actual  : " + str(actual))
    assert actual == desired
    print()

    s = "listen"
    t = "silent"
    actual = Solution.isAnagram(Solution, s, t)
    desired = True
    print("s, t: %s %s " % (s, t))
    print("desired : " + str(desired))
    print("actual  : " + str(actual))
    assert actual == desired
    print()

    s = "listena"
    t = "silent"
    actual = Solution.isAnagram(Solution, s, t)
    desired = False
    print("s, t: %s %s " % (s, t))
    print("desired : " + str(desired))
    print("actual  : " + str(actual))
    assert actual == desired
    print()

    s = "a"
    t = "a"
    actual = Solution.isAnagram(Solution, s, t)
    desired = True
    print("s, t: %s %s " % (s, t))
    print("desired : " + str(desired))
    print("actual  : " + str(actual))
    assert actual == desired
    print()

    s = ""
    t = ""
    actual = Solution.isAnagram(Solution, s, t)
    desired = True
    print("s, t: %s %s " % (s, t))
    print("desired : " + str(desired))
    print("actual  : " + str(actual))
    assert actual == desired
    print()

    s = "a"
    t = ""
    actual = Solution.isAnagram(Solution, s, t)
    desired = False
    print("s, t: %s %s " % (s, t))
    print("desired : " + str(desired))
    print("actual  : " + str(actual))
    assert actual == desired
    print()
