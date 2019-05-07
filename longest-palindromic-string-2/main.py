class Solution(object):
    def longestPalindrome(Self, s):
        if len(s) = 0:
            return ""
        evenPals = [[i, i + 1] for i in range(len(s))[:-1] if s[i] == s[i + 1]]
        growing = True
        while (growing):
            growing = False
            for palIndex in range(len(evenPals)):
                if evenPals[palIndex] is None:
                    continue
                if len(evenPals[palIndex]) == 1:
                    lcand = evenPals[palIndex][0]
                    ucand = evenPals[palIndex][0]
                else:
                    lcand = evenPals[palIndex][-2] - 1
                    ucand = evenPals[palIndex][-1] + 1
                if lcand > -1 and lcand < len(s) and ucand > -1 and ucand < len(s) and s[lcand] == s[ucand]:
                    growing = True
                    evenPals[palIndex].append(lcand)
                    evenPals[palIndex].append(ucand)

            longestEven = ""
            if len(evenPals) > 0:
                max = len(evenPals[0])
                maxIndex = 0
                for palIndex in range(len(evenPals)):
                    if len(evenPals[palIndex]) > max:
                        max = len(evenPals[palIndex])
                        maxIndex = palIndex
                for palIndex in range(len(evenPals)):
                    if len(evenPals[palIndex]) < max:
                        evenPals[palIndex] == None
                for i in sorted(evenPals[maxIndex]):
                    longestEven += s[i]

        oddPals = [[i] for i in range(len(s))]
        growing = True
        while (growing):
            growing = False
            for palIndex in range(len(oddPals)):
                if oddPals[palIndex] is None:
                    continue
                if len(oddPals[palIndex]) == 1:
                    lcand = oddPals[palIndex][0] - 1
                    ucand = oddPals[palIndex][0] + 1
                else:
                    lcand = oddPals[palIndex][-2] - 1
                    ucand = oddPals[palIndex][-1] + 1
                if lcand > -1 and lcand < len(s) and ucand > -1 and ucand < len(s) and s[lcand] == s[ucand]:
                    growing = True
                    oddPals[palIndex].append(lcand)
                    oddPals[palIndex].append(ucand)

            max = len(oddPals[0])
            maxIndex = 0
            for palIndex in range(len(oddPals)):
                if len(oddPals[palIndex]) > max:
                    max = len(oddPals[palIndex])
                    maxIndex = palIndex

            for palIndex in range(len(oddPals)):
                if len(oddPals[palIndex]) < max:
                    oddPals[palIndex] == None

            longestOdd = ""
            for i in sorted(oddPals[maxIndex]):
                longestOdd += s[i]

        ans = longestOdd
        if len(longestEven) > len(longestOdd):
            ans = longestEven

        return ans


if __name__ == '__main__':
    input = "abba"
    output = input
    actual = Solution.longestPalindrome(Solution, input)
    print("input input: % s" % input)
    print("target output: %s" % output)
    print("actual output: %s" % actual)
    print()

    input = "cabbac"
    output = input
    actual = Solution.longestPalindrome(Solution, input)
    print("input input: % s" % input)
    print("target output: %s" % output)
    print("actual output: %s" % actual)
    print()

    input = "cabbacii"
    output = "cabbac"
    actual = Solution.longestPalindrome(Solution, input)
    print("input input: % s" % input)
    print("target output: %s" % output)
    print("actual output: %s" % actual)
    print()

    input = "jcabbacii"
    output = "cabbac"
    actual = Solution.longestPalindrome(Solution, input)
    print("input input: % s" % input)
    print("target output: %s" % output)
    print("actual output: %s" % actual)
    print()

    input = "bb"
    output = "bb"
    actual = Solution.longestPalindrome(Solution, input)
    print("input input: % s" % input)
    print("target output: %s" % output)
    print("actual output: %s" % actual)
    print()
    #
    input = "bbc"
    output = "bb"
    actual = Solution.longestPalindrome(Solution, input)
    print("input input: % s" % input)
    print("target output: %s" % output)
    print("actual output: %s" % actual)
    print()
    #
    input = "bbc"
    output = "b"
    actual = Solution.longestPalindrome(Solution, input)
    print("input input: % s" % input)
    print("target output: %s" % output)
    print("actual output: %s" % actual)
    print()

    input = "aba"
    output = "aba"
    actual = Solution.longestPalindrome(Solution, input)
    print("input input: % s" % input)
    print("target output: %s" % output)
    print("actual output: %s" % actual)
    print()

    input = "ubbcbbjjjj"
    output = "bbcbb"
    actual = Solution.longestPalindrome(Solution, input)
    print("input input: % s" % input)
    print("target output: %s" % output)
    print("actual output: %s" % actual)
    print()

