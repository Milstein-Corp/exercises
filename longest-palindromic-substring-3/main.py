class Solution(object):
    def longestPalindrome(self, input):
        if len(input) == 0:
            return ""
        if len(input) == 1:
            return input

        odd_pals = []
        for i in range(len(input)):
            odd_pals.append([i, i])
        odd_pal = Solution.long(Solution, odd_pals, input)

        even_pals = []
        for i in range(len(input)-1):
            if input[i] == input[i+1]:
                even_pals.append([i, i+1])
        even_pal = Solution.long(Solution, even_pals, input)

        if len(even_pal) > len(odd_pal):
            return even_pal
        else:
            return odd_pal

    def long(self, pals, input):
        """
        takes a list of pal seeds, returns the longest pal out of the seeds"
        :param pals:
        :return:
        """
        growing = True
        while growing:
            growing = False
            for pal in pals:
                if pal is None:
                    continue
                # cand1 < cand2, and smaller values are placed before larger values
                cand1 = pal[-2] - 1
                cand2 = pal[-1] + 1

                if -1 < cand1 < len(input) \
                        and -1 < cand2 < len(input) \
                        and input[cand1] == input[cand2]:
                    growing = True
                    pal.append(cand1)
                    pal.append(cand2)
            max = -1
            for pal in pals:
                if pal is not None and len(pal) > max:
                    max = len(pal)
            for p in range(len(pals)):
                if pals[p] is not None and len(pals[p]) != max:
                    pals[p] = None

        best_pal = []
        for pal in pals:
            if pal is not None and len(pal) == max:
                best_pal = pal

        if best_pal and best_pal[0] == best_pal[1]:
            del best_pal[0]

        ans = ""
        for c in sorted(best_pal):
            ans = ans + (input[c])

        return ans

if __name__ == '__main__':
    input = "aba"
    desired = "aba"
    actual = Solution.longestPalindromicSubstring(Solution, input)
    print("testing")
    print("input: %s" % input)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    input = "cabac"
    desired = "cabac"
    actual = Solution.longestPalindromicSubstring(Solution, input)
    print("input: %s" % input)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    input = "cabackasdjfka"
    desired = "cabac"
    actual = Solution.longestPalindromicSubstring(Solution, input)
    print("input: %s" % input)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    input = "asdfddwcabackasdjfka"
    desired = "cabac"
    actual = Solution.longestPalindromicSubstring(Solution, input)
    print("input: %s" % input)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    input = "a"
    desired = "a"
    actual = Solution.longestPalindromicSubstring(Solution, input)
    print("input: %s" % input)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    input = ""
    desired = ""
    actual = Solution.longestPalindromicSubstring(Solution, input)
    print("input: %s" % input)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    input = "baab"
    desired = "baab"
    actual = Solution.longestPalindromicSubstring(Solution, input)
    print("input: %s" % input)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    input = "baabc"
    desired = "baab"
    actual = Solution.longestPalindromicSubstring(Solution, input)
    print("input: %s" % input)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    input = "aa"
    desired = "aa"
    actual = Solution.longestPalindromicSubstring(Solution, input)
    print("input: %s" % input)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    input = "asdfasdgaagoiupo"
    desired = "gaag"
    actual = Solution.longestPalindromicSubstring(Solution, input)
    print("input: %s" % input)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()




