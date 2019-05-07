class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        oddpals = [[i] for i in range(len(s))]
        winner = 0
        growing = True
        while (growing):
            # grow
            growing = False
            for pal in oddpals:
                if pal == None:
                    continue
                if len(pal) == 1:
                    cand1 = pal[0] - 1
                    cand2 = pal[0] + 1
                else:
                    cand1 = pal[-2] - 1
                    cand2 = pal[-1] + 1
                if cand1 >= 0 and cand2 >= 0 and cand1 < len(s) and cand2 < len(s) and s[cand1] == s[cand2]:
                    pal.append(cand1)
                    pal.append(cand2)
                    growing = True
            max = 0
            for pal in oddpals:
                if pal and max < len(pal):
                    max = len(pal)
            for i in range(len(oddpals)):
                if oddpals[i] and len(oddpals[i]) < max:
                    oddpals[i] = None

        evenpals = [[i, i +1] for i in range(len(s))[:-1] if s[i] == s[i+1]]
        # if len(s) == 2 and s[0] == s[1]:
        #     evenpals = [[0, 1]]

        winner = 0
        growing = True
        while (growing):
            # grow
            growing = False
            for pal in evenpals:
                if pal == None:
                    continue
                if len(pal) == 2:
                    cand1 = pal[0] - 1
                    cand2 = pal[1] + 1
                else:
                    cand1 = pal[-2] - 1
                    cand2 = pal[-1] + 1
                if cand1 >= 0 and cand2 >= 0 and cand1 < len(s) and cand2 < len(s) and s[cand1] == s[cand2]:
                    pal.append(cand1)
                    pal.append(cand2)
                    growing = True

            max = 0
            for pal in evenpals:
                if pal and max < len(pal):
                    max = len(pal)

            for i in range(len(evenpals)):
                if evenpals[i] and len(evenpals[i]) < max:
                    evenpals[i] = None

        maxlen = 0
        max = ""
        for pal in evenpals:
            if pal != None and len(pal) > maxlen:
                maxlen = len(pal)
                max = pal
        for pal in oddpals:
            if pal != None and len(pal) > maxlen:
                maxlen = len(pal)
                max = pal
        max = sorted(max)
        max = [s[i] for i in max]
        return "".join(max)


def main():
    input = "abbbba"
    output = input
    a = Solution.longestPalindrome(Solution, input)
    print("desired output: %s" % output)
    print("actual output: %s" % a)
    print()

    input = "abbbbac"
    output = "abbbbac"
    a = Solution.longestPalindrome(Solution, input)
    print("desired output: %s" % output)
    print("actual output: %s" % a)
    print()

    input = "abcba"
    output = input
    a = Solution.longestPalindrome(Solution, input)
    print("desired output: %s" % output)
    print("actual output: %s" % a)
    print()

    input = "sadfasdfabcbahhh"
    output = "abcba"
    a = Solution.longestPalindrome(Solution, input)
    print("desired output: %s" % output)
    print("actual output: %s" % a)
    print()

    input = "abca"
    output = "a"
    a = Solution.longestPalindrome(Solution, input)
    print("desired output: %s" % output)
    print("actual output: %s" % a)
    print()

    input = "bb"
    output = "bb"
    a = Solution.longestPalindrome(Solution, input)
    print("desired output: %s" % output)
    print("actual output: %s" % a)
    print()

    input = "bbc"
    output = "bb"
    a = Solution.longestPalindrome(Solution, input)
    print("desired output: %s" % output)
    print("actual output: %s" % a)
    print()

    input = ""
    output = ""
    a = Solution.longestPalindrome(Solution, input)
    print("desired output: %s" % output)
    print("actual output: %s" % a)
    print()
    #
    print()


if __name__ == '__main__':
    main()
