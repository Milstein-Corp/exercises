class Solution(object):
    def fit(self, word, s):
        """fit checks to see if word fits at the front
        of the string s. The strategy is to try to return False early"""
        if len(word) > len(s):
            return False

        for c in range(len(word)):
            if not word[c] == s[c]:
                return False

        return True

    def wordBreak(self, s, wordDict):
        words = wordDict
        paths = []
        lengths = []

        for word in words:
            if Solution.fit(Solution, word, s):
                paths.append(len(word))
                lengths.append(len(word))

        if not paths:
            return False
        # Pathes is not empty. It might have the final path

        # try to find a path
        while paths:
            examine = paths.pop()
            if examine == len(s):
                return True

            for word in words:
                if Solution.fit(Solution, word, s[examine:]):
                    if examine + len(word) not in lengths:
                        paths.append(examine + len(word))
                        lengths.append(examine + len(word))

        return False

if __name__ == '__main__':
    s = "aba"
    wordDict = ["that", "a", "b"]
    actual = Solution.wordBreak(Solution, s, wordDict)
    desired = True
    print(s)
    print(wordDict)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    s = "abaaaa"
    wordDict = ["that", "a", "b"]
    actual = Solution.wordBreak(Solution, s, wordDict)
    desired = True
    print(s)
    print(wordDict)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    s = "abaaaa"
    wordDict = ["that", "b"]
    actual = Solution.wordBreak(Solution, s, wordDict)
    desired = False
    print(s)
    print(wordDict)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    s = "abaaaa"
    wordDict = []
    actual = Solution.wordBreak(Solution, s, wordDict)
    desired = False
    print(s)
    print(wordDict)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    s = ""
    wordDict = ["that"]
    actual = Solution.wordBreak(Solution, s, wordDict)
    desired = False
    print(s)
    print(wordDict)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    s = ""
    wordDict = []
    actual = Solution.wordBreak(Solution, s, wordDict)
    desired = False
    print(s)
    print(wordDict)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    s = "catdogpenpencil"
    wordDict = ['cat', 'dog', 'pen', 'pencil']
    actual = Solution.wordBreak(Solution, s, wordDict)
    desired = True
    print(s)
    print(wordDict)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    s = "catdogpenpencil"
    wordDict = ['cat', 'dog', 'pen']
    actual = Solution.wordBreak(Solution, s, wordDict)
    desired = False
    print(s)
    print(wordDict)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    s = "aaaaaaa"
    wordDict = ['aaaa', 'aa', 'aa']
    actual = Solution.wordBreak(Solution, s, wordDict)
    desired = False
    print(s)
    print(wordDict)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

