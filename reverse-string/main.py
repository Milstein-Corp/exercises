# Definition for singly-linked list.

class Solution(object):
    def reverseStringd(self, s):
        """95 percentile runtime"""
        n = int(len(s)//2)

        for i in range(n):
            s[i], s[-i-1] = s[-i-1], s[i]

        return s

    def reverseString(self, s):
        """95 percentile runtime"""
        i, j = 0, len(s)-1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

        return s



if __name__ == '__main__':
    s = ["r", "a", "c", "e", "c", "a"]
    actual = Solution.reverseString(Solution, s.copy())
    print("input: " + str(s))
    print("actual: " + str(actual))
    print("desired: " + str(s[::-1]))
    assert actual == s[::-1]
    print()

    s = ["r", "a", "c", "e", "c", "a", "b"]
    actual = Solution.reverseString(Solution, s.copy())
    print("input: " + str(s))
    print("actual: " + str(actual))
    print("desired: " + str(s[::-1]))
    assert actual == s[::-1]
    print()

    s = ["r", "a"]
    actual = Solution.reverseString(Solution, s.copy())
    print("input: " + str(s))
    print("actual: " + str(actual))
    print("desired: " + str(s[::-1]))
    assert actual == s[::-1]
    print()

    s = ["r"]
    actual = Solution.reverseString(Solution, s.copy())
    print("input: " + str(s))
    print("actual: " + str(actual))
    print("desired: " + str(s[::-1]))
    assert actual == s[::-1]
    print()

    s = []
    actual = Solution.reverseString(Solution, s.copy())
    print("input: " + str(s))
    print("actual: " + str(actual))
    print("desired: " + str(s[::-1]))
    assert actual == s[::-1]
    print()
