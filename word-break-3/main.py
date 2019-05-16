class Solution(object):
    def fit(self, word, s):
        if len(word) > len(s):
            return False

        for c in range(len(word)):
            if word[c] != s[c]:
                return False

        return True

    def wordBreak(self, s, wordDict):
        paths = []
        lengths = []

        for word in wordDict:
            if Solution.fit(Solution, word, s):
                paths.append(len(word))
                lengths.append(len(word))

        while paths:
            path = paths.pop()
            if path == len(s):
                return True
            else:
                for word in words:
                    proposed = len(word) + path
                    if proposed not in lengths and Solution.fit(Solution, word, s[path:]):
                        paths.append(proposed)
                        lengths.append(proposed)

        return False


if __name__ == '__main__':
    s = "penpencil"
    words = ["pen", "pencil"]
    desired = True
    actual = Solution.wordBreak(Solution, s, words)
    print("s: %s" % s)
    print("words: %s" % words)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    s = "penpencild"
    words = ["pen", "pencil"]
    desired = False
    actual = Solution.wordBreak(Solution, s, words)
    print("s: %s" % s)
    print("words: %s" % words)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    s = "penpencilpenpenpenpen"
    words = ["pen", "pencil"]
    desired = True
    actual = Solution.wordBreak(Solution, s, words)
    print("s: %s" % s)
    print("words: %s" % words)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    s = "aaaaaa"
    words = ["aaaa", "aa"]
    desired = True
    actual = Solution.wordBreak(Solution, s, words)
    print("s: %s" % s)
    print("words: %s" % words)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    s = "aaaaaaa"
    words = ["aaaa", "aa"]
    desired = False
    actual = Solution.wordBreak(Solution, s, words)
    print("s: %s" % s)
    print("words: %s" % words)
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

