class Solution(object):
    def longestPal(self, s):
        if len(s) == 0:
            return ""
        if len(s) == 1:
            return s

        pals = []
        for c in range(0, len(s)-1):
            pals.append((c, c))
            if s[c] == s[c+1]:
                pals.append((c, c+1))
        pals.append((len(s)-1, len(s)-1))

        longestPal = pals[0]
        while pals:
            pal = pals.pop()
            if 0 != pal[0] and pal[1] != len(s) - 1 \
                and s[pal[0]-1] == s[pal[1]+1]:
                pals.append((pal[0]-1, pal[1]+1))
            elif pal[1] - pal[0] > longestPal[1] - longestPal[0]:
                longestPal = pal

        ans = [s[i] for i in range(longestPal[0], longestPal[1]+1)]

        return "".join(ans)


if __name__ == '__main__':
    input = "ana"
    actual = Solution.longestPal(Solution, input)
    desired = "ana"
    print("input: %s" % input)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    input = "anaiii"
    actual = Solution.longestPal(Solution, input)
    desired = "iii"
    print("input: %s" % input)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    input = "mnanaiik"
    actual = Solution.longestPal(Solution, input)
    desired = "ana"
    print("input: %s" % input)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    input = "mnpqkmanaiik"
    actual = Solution.longestPal(Solution, input)
    desired = "ana"
    print("input: %s" % input)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    input = "aa"
    actual = Solution.longestPal(Solution, input)
    desired = "aa"
    print("input: %s" % input)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()
