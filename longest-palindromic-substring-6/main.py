class Solution(object):
    def longestPalindrome(self, example):
        if len(example) == 0:
            return ''
        elif len(example) == 1:
            return example

        pals = []
        if example[0] == example[1]:
            pals.append([0, 1])

        for i in range(1, len(example) - 1):
            if example[i - 1] == example[i + 1]:
                pals.append([i, i - 1, i + 1])
            if example[i] == example[i + 1]:
                pals.append([i, i + 1])

        longestPal = [0]
        palLen = 1

        while pals:
            pal = pals.pop()
            cand1 = pal[-2] - 1
            cand2 = pal[-1] + 1
            if -1 < cand1 < len(example) and \
                    -1 < cand2 < len(example) and \
                    example[cand1] == example[cand2]:
                pal.append(cand1)
                pal.append(cand2)
                pals.append(pal)
            elif len(pal) > palLen:
                longestPal = pal
                palLen = len(pal)

        ans = [example[c] for c in sorted(longestPal)]

        return "".join(ans)


if __name__ == '__main__':
    example = "aaaa"
    desired = "aba"
    actual = Solution.longestPalindrome(Solution, example)
    print("example: %s" % example)
    print("desired: %s" % desired)
    print("acutal: %s " % actual)
    print()

    example = "abaa"
    desired = "aba"
    actual = Solution.longestPalindrome(Solution, example)
    print("example: %s" % example)
    print("desired: %s" % desired)
    print("acutal: %s " % actual)
    print()
    #
    example = "aabaa"
    desired = "aabaa"
    actual = Solution.longestPalindrome(Solution, example)
    print("example: %s" % example)
    print("desired: %s" % desired)
    print("acutal: %s " % actual)
    print()

    example = "aabaaa"
    desired = "aabaa"
    actual = Solution.longestPalindrome(Solution, example)
    print("example: %s" % example)
    print("desired: %s" % desired)
    print("acutal: %s " % actual)
    print()

    example = "aabaasdfasdfasdf"
    desired = "aabaa"
    actual = Solution.longestPalindrome(Solution, example)
    print("example: %s" % example)
    print("desired: %s" % desired)
    print("acutal: %s " % actual)
    print()

    example = "werweraabaammbmnb"
    desired = "aabaa"
    actual = Solution.longestPalindrome(Solution, example)
    print("example: %s" % example)
    print("desired: %s" % desired)
    print("acutal: %s " % actual)
    print()

    example = "aa"
    desired = "aa"
    actual = Solution.longestPalindrome(Solution, example)
    print("example: %s" % example)
    print("desired: %s" % desired)
    print("acutal: %s " % actual)
    print()

    example = "a"
    desired = "a"
    actual = Solution.longestPalindrome(Solution, example)
    print("example: %s" % example)
    print("desired: %s" % desired)
    print("acutal: %s " % actual)
    print()

    example = "aaaa"
    desired = "aaaa"
    actual = Solution.longestPalindrome(Solution, example)
    print("example: %s" % example)
    print("desired: %s" % desired)
    print("acutal: %s " % actual)
    print()

