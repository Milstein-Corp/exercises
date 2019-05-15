class Solution(object):
    def longestPalindrome(self, input):
        if not input:
            return ""

        pals = []
        for c in range(len(input)-1):
            pals.append([c])
            if input[c] == input[c+1]:
                pals.append([c, c+1])
        pals.append([len(input)-1])

        # pals needs to be non-empty
        longest = pals[0]
        while pals:
            # pals is not empty
            examine = pals.pop()
            if len(examine) > len(longest):
                longest = examine

            if len(examine) == 1:
                cand1 = examine[0] - 1
                cand2 = examine[0] + 1
            else:
                cand1 = examine[-2] - 1
                cand2 = examine[-1] + 1

            if -1 < cand1 < len(input) and \
                -1 < cand2 < len(input) and \
                    input[cand1] == input[cand2]:
                examine.append(cand1)
                examine.append(cand2)
                pals.append(examine)

        cha = [input[i] for i in sorted(longest)]

        return "".join(cha)


if __name__ == '__main__':
    input = "aba"
    desired = "aba"
    actual = Solution.longestPalindrom(Solution, input)
    print("input: %s" % input)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    input = "cabac"
    desired = "cabac"
    actual = Solution.longestPalindrom(Solution, input)
    print("input: %s" % input)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    input = "cabacsdfa"
    desired = "cabac"
    actual = Solution.longestPalindrom(Solution, input)
    print("input: %s" % input)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    input = "iuyyicabacsdfa"
    desired = "cabac"
    actual = Solution.longestPalindrom(Solution, input)
    print("input: %s" % input)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    input = "e"
    desired = "e"
    actual = Solution.longestPalindrom(Solution, input)
    print("input: %s" % input)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    input = "qwertyu"
    desired = "q"
    actual = Solution.longestPalindrom(Solution, input)
    print("input: %s" % input)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()


    input = ""
    desired = ""
    actual = Solution.longestPalindrom(Solution, input)
    print("input: %s" % input)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    input = "aa"
    desired = "aa"
    actual = Solution.longestPalindrom(Solution, input)
    print("input: %s" % input)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    input = "abba"
    desired = "abba"
    actual = Solution.longestPalindrom(Solution, input)
    print("input: %s" % input)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    input = "abbaiuoiiiu"
    desired = "abba"
    actual = Solution.longestPalindrom(Solution, input)
    print("input: %s" % input)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    input = "reweewrabbaiuoiiiu"
    desired = "abba"
    actual = Solution.longestPalindrom(Solution, input)
    print("input: %s" % input)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()


