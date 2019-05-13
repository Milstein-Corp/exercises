class Solution(object):
    def expand(self, pals, input):
        growing = True
        while growing: # pals is non-empty
            growing = False
            for pal in pals:
                if pal is None:
                    continue
                cand1 = pal[-2] - 1
                cand2 = pal[-1] + 1
                if -1 < cand1 < len(input) and -1 < cand2 < len(input) and input[cand1] == input[cand2]:
                    growing = True
                    pal.append(cand1)
                    pal.append(cand2)
            maxlen = len(max(filter(None, pals), key=len))

            for p in range(len(pals)):
                if pals[p] and len(pals[p]) != maxlen:
                    pals[p] = None
            # We are guaranteed a non empty list with pals here
        return pals

    def longestPalindrome(self, input):
        odd_pals = []
        for i in range(len(input)):
            odd_pals.append([i, i])
        if odd_pals:
            odd_pals = Solution.expand(Solution, odd_pals, input)
            best_odd_pal = next(filter(None, odd_pals))[1:]
            odd_answer = [input[a] for a in sorted(best_odd_pal)]
        else:
            odd_answer = ''

        even_pals = []
        for i in range(len(input[:-1])):
            if input[i] == input[i+1]:
                even_pals.append([i, i+1])
        if even_pals:
            even_pals = Solution.expand(Solution, even_pals, input)
            best_pal = next(filter(None, even_pals))
            even_answer = [input[a] for a in sorted(best_pal)]
        else:
            even_answer = ''

        final_answer = max(odd_answer, even_answer, key=len)

        return "".join(final_answer)


if __name__ == '__main__':
    input = "aba"
    desired = "aba"
    actual = Solution.longestPalindrome(Solution, input)
    print("input: %s" % input)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    input = "cabac"
    desired = "cabac"
    actual = Solution.longestPalindrome(Solution, input)
    print("input: %s" % input)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    input = "cabacadskjfasdh"
    desired = "cabac"
    actual = Solution.longestPalindrome(Solution, input)
    print("input: %s" % input)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    input = "cabbac"
    desired = "cabbac"
    actual = Solution.longestPalindrome(Solution, input)
    print("input: %s" % input)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    input = "aa"
    desired = "aa"
    actual = Solution.longestPalindrome(Solution, input)
    print("input: %s" % input)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    input = "ccabacciiii"
    desired = "ccabacc"
    actual = Solution.longestPalindrome(Solution, input)
    print("input: %s" % input)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    input = "asdfasdfcabacadskjfasdh"
    desired = "cabac"
    actual = Solution.longestPalindrome(Solution, input)
    print("input: %s" % input)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    input = "cabbaciuiuiuiu"
    desired = "cabbac"
    actual = Solution.longestPalindrome(Solution, input)
    print("input: %s" % input)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    input = "h"
    desired = "h"
    actual = Solution.longestPalindrome(Solution, input)
    print("input: %s" % input)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    input = ""
    desired = ""
    actual = Solution.longestPalindrome(Solution, input)
    print("input: %s" % input)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()




