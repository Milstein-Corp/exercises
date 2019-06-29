class Solution(object):
    def validPalindrome(self, s):

        isPal = True
        for i in range(len(s)):
            if s[i] == s[-1-i]:
                pass
            else:
                isPal = False  # we are gonna go do that other loop
                falsei = i  # this is the element that didn't work
                break
        if isPal:
            return isPal


        isPal = True
        modify_1 = list(s)
        del modify_1[falsei]
        modify_1 = "".join(modify_1)
        for i in range(len(modify_1)):
            if modify_1[i] == modify_1[-1-i]:
                pass
            else:
                isPal = False
                break
        if isPal:
            return isPal


        isPal = True
        modify_1 = list(s)
        del modify_1[-1-falsei]
        modify_1 = "".join(modify_1)
        for i in range(len(modify_1)):
            if modify_1[i] == modify_1[-1-i]:
                pass
            else:
                isPal = False  # we are gonna go do that other loop
                break
        if isPal:
            return isPal

        return False


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

