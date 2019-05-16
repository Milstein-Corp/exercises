class Solution(object):
    def longestPalindrome(self, s):
        if s == '':
            return ''
        elif len(s) == 1:
            return s[0]

        pals = []
        if s[0] == s[1]: # xxxx
            pals.append((0, 2))

        for i in range(1, len(s) - 1):
            if s[i] == s[i + 1]: # xxxx
                pals.append((i, 2))
            if s[i - 1] == s[i + 1]: # xxxx
                pals.append((i, 3))

        if not pals:
            return s[0]

        longestPal = (0, 1)

        while pals:
            pal = pals.pop()

            if pal[1] % 2 == 0:
                cand1 = pal[0] + 1 + (pal[1] - 2) / 2 + 1 # xxx
                cand2 = pal[0] - (pal[1] - 2) / 2 - 1
            else:
                cand1 = pal[0] + (pal[1] - 1) / 2 + 1
                cand2 = pal[0] - (pal[1] - 1) / 2 - 1
            cand1 = int(cand1)
            cand2 = int(cand2)

            if -1 < cand1 < len(s) and -1 < cand2 < len(s) \
                    and s[cand1] == s[cand2]:
                newpal = (pal[0], pal[1] + 2)
                pals.append(newpal)
            elif pal[1] > longestPal[1]:
                longestPal = pal

        firstIndex = -1
        if longestPal[1] % 2 == 0:
            firstIndex = int(longestPal[0] - (longestPal[1] - 2)/2)
        else:
            firstIndex = int(longestPal[0] - (longestPal[1] - 1)/2)


        pal = [i for i in range(firstIndex, firstIndex + longestPal[1])]
        stringpal = "".join([input[i] for i in sorted(pal)])

        return stringpal


if __name__ == '__main__':
    input = "aba"
    desired = "aba"
    actual = Solution.longestPalindrome(Solution, input)
    actual = str(actual)
    print("input: %s" % input)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    input = "abaa"
    desired = "aba"
    actual = Solution.longestPalindrome(Solution, input)
    actual = str(actual)
    print("input: %s" % input)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    input = "aa"
    desired = "aa"
    actual = Solution.longestPalindrome(Solution, input)
    actual = str(actual)
    print("input: %s" % input)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    input = "cabac"
    desired = "cabac"
    actual = Solution.longestPalindrome(Solution, input)
    actual = str(actual)
    print("input: %s" % input)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    input = "bbbb"
    desired = "bbbb"
    actual = Solution.longestPalindrome(Solution, input)
    actual = str(actual)
    print("input: %s" % input)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    input = "bbaabb"
    desired = "bbaabb"
    actual = Solution.longestPalindrome(Solution, input)
    actual = str(actual)
    print("input: %s" % input)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    input = "bbaabbiouiuouyy"
    desired = "bbaabb"
    actual = Solution.longestPalindrome(Solution, input)
    actual = str(actual)
    print("input: %s" % input)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    input = "rrebbaabbiouiuouyy"
    desired = "bbaabb"
    actual = Solution.longestPalindrome(Solution, input)
    actual = str(actual)
    print("input: %s" % input)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()
