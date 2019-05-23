class Solution(object):
    def fit(self, word, s):
        if len(word) > len(s):
            return False
        for w in range(len(word)):
            if word[w] != s[w]:
                return False
        return True

    def wordBreak(self, s, wordDict):
        paths = []
        lengths = []
        for word in wordDict:
            if Solution.fit(Solution, word, s) and len(word) not in lengths:
                paths.append(len(word))
                lengths.append(len(word))
        ans = []

        while paths:
            path = paths.pop()
            if path == len(s):
                return True
            else:
                for word in wordDict:
                    if Solution.fit(Solution, word, s[path:]) \
                            and len(word)+path not in lengths:
                        paths.append(len(word)+path)
                        lengths.append(len(word)+path)

        return False


if __name__ == '__main__':
    s = "penpen"
    wordDict = ["pen", "grate"]
    actual = Solution.wordBreak(Solution, s, wordDict)
    desired = True
    print("s: % s" % s)
    print("wordDict: % s " % wordDict)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    s = "penpeni"
    wordDict = ["pen", "grate"]
    actual = Solution.wordBreak(Solution, s, wordDict)
    desired = False
    print("s: % s" % s)
    print("wordDict: % s " % wordDict)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    s = "penpencil"
    wordDict = ["pen", "pencil"]
    actual = Solution.wordBreak(Solution, s, wordDict)
    desired = True
    print("s: % s" % s)
    print("wordDict: % s " % wordDict)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    s = "penpencilr"
    wordDict = ["pen", "pencil"]
    actual = Solution.wordBreak(Solution, s, wordDict)
    desired = False
    print("s: % s" % s)
    print("wordDict: % s " % wordDict)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

