class Solution(object):
    def same(self, w1, w2):
        for c in range(len(w2)):
            if w1[c] != w2[c]:
                return False

        return True

    def strStr(self, haystack, needle):
        if needle == '':
            return 0

        size = len(needle)
        found = -1

        for i in range(0, len(haystack) - size + 1):
            if Solution.same(Solution, haystack[i:i + size], needle):
                found = i
                break

        return found


if __name__ == '__main__':
    hay = "hello"
    needle = "ll"
    actual = Solution.strStr(Solution, hay, needle)
    desired = 2
    print("actual: %s" % actual)
    print("desired: %s" % desired)
    print()

    hay = "hello"
    needle = "o"
    actual = Solution.strStr(Solution, hay, needle)
    desired = 4
    print("actual: %s" % actual)
    print("desired: %s" % desired)
    print()

    hay = "hello"
    needle = "el"
    actual = Solution.strStr(Solution, hay, needle)
    desired = 1
    print("actual: %s" % actual)
    print("desired: %s" % desired)
    print()

    hay = "hellobobyouarezakbegin"
    needle = "zak"
    actual = Solution.strStr(Solution, hay, needle)
    desired = 14
    print("actual: %s" % actual)
    print("desired: %s" % desired)
    print()

    hay = "aaa"
    needle = "a"
    actual = Solution.strStr(Solution, hay, needle)
    desired = 0
    print("actual: %s" % actual)
    print("desired: %s" % desired)
    print()
