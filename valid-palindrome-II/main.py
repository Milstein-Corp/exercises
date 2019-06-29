class Solution(object):
    def validPalindrome(self, s):
        i = 0
        length = len(s)
        j = length - 1
        s = list(s)
        while j > i:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return s[i+1:j+1] == s[i+1:j+1:][::-1] or s[i:j] == s[i:j][::-1]

        return True


if __name__ == '__main__':
    s = "aba"
    desired = True
    actual = Solution.validPalindrome(Solution, s)
    print("arguments: %s" % s)
    print("desired : " + str(desired))
    print("actual  : " + str(actual))
    assert desired == actual
    print()

    s = "cabac"
    desired = True
    actual = Solution.validPalindrome(Solution, s)
    print("arguments: %s" % s)
    print("desired : " + str(desired))
    print("actual  : " + str(actual))
    assert desired == actual
    print()

    s = "cabbac"
    desired = True
    actual = Solution.validPalindrome(Solution, s)
    print("arguments: %s" % s)
    print("desired : " + str(desired))
    print("actual  : " + str(actual))
    assert desired == actual
    print()

    s = "cakbbac"
    desired = True
    actual = Solution.validPalindrome(Solution, s)
    print("arguments: %s" % s)
    print("desired : " + str(desired))
    print("actual  : " + str(actual))
    assert desired == actual
    print()

    s = "cabbaeec"
    desired = False
    actual = Solution.validPalindrome(Solution, s)
    print("arguments: %s" % s)
    print("desired : " + str(desired))
    print("actual  : " + str(actual))
    assert desired == actual
    print()

    s = "cabbbbaaac"
    desired = False
    actual = Solution.validPalindrome(Solution, s)
    print("arguments: %s" % s)
    print("desired : " + str(desired))
    print("actual  : " + str(actual))
    assert desired == actual
    print()
    #
    s = "c"
    desired = True
    actual = Solution.validPalindrome(Solution, s)
    print("arguments: %s" % s)
    print("desired : " + str(desired))
    print("actual  : " + str(actual))
    assert desired == actual
    print()

    s = ""
    desired = True
    actual = Solution.validPalindrome(Solution, s)
    print("arguments: %s" % s)
    print("desired : " + str(desired))
    print("actual  : " + str(actual))
    assert desired == actual
    print()

    s = "aai"
    desired = True
    actual = Solution.validPalindrome(Solution, s)
    print("arguments: %s" % s)
    print("desired : " + str(desired))
    print("actual  : " + str(actual))
    assert desired == actual
    print()

    s = "xxxukxxx"
    desired = True
    actual = Solution.validPalindrome(Solution, s)
    print("arguments: %s" % s)
    print("desired : " + str(desired))
    print("actual  : " + str(actual))
    assert desired == actual
    print()
