class Solution(object):
    def match(self, w, words, rest):
        is_match = True
        for c in range(len(words[w])):
            if len(words[w]) <= len(rest) and words[w][c] == rest[c]:
                y = 2
            else:
                is_match = False
                break
        return is_match

    def wordBreak(self, s, wordDict):
        a1 = set(s)
        a2 = set()
        for w in wordDict:
            for c in w:
                a2.add(c)
        if not a1.issubset(a2):
            return False
        words = wordDict

        paths = []
        farthest = 0
        for w in range(len(words)):
            if words[w] == s[:len(words[w])]:
                paths.append([w])
                if len(words[w]) > farthest:
                    farthest = len(words[w])
        if paths:
            growing = True
        else:
            growing = False
        answer = False
        while growing:
            new_paths = []
            growing = False

            for path in paths:
                path_length = 0
                for w in path:
                    path_length += len(words[w])
                rest = s[path_length:]  # this will throw an error, if path_length too big. Shouldn't.
                if not rest:  # the path was already good.
                    new_paths.append(path)
                    answer = True
                else:
                    for w in range(len(words)):
                        new_path = list.copy(path)
                        is_match = Solution.match(Solution, w, words, rest)
                        if is_match:
                            growing = True
                            new_path.append(w)
                            new_paths.append(new_path)
            paths = new_paths

            new_paths = []
            lengths = []
            for path in paths:
                if len(path) not in lengths:
                    lengths.append(len(path))
                    new_paths.append(path)
            paths = new_paths


        return answer


if __name__ == '__main__':
    s = "penapepen"
    wordDict = ["pen", "ape"]
    actual = Solution.wordBreak(Solution, s, wordDict)
    desired = [[0, 1, 0]]
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    s = "pencilpen"
    wordDict = ["pen", "pencil", "cil"]
    actual = Solution.wordBreak(Solution, s, wordDict)
    desired = [[0, 2, 0], [1, 0]]
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    s = "pencilpen"
    wordDict = ["pen", "pencil", "cil"]
    actual = Solution.wordBreak(Solution, s, wordDict)
    desired = [[0, 2, 0], [1, 0]]
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    s = "pencilpeng"
    wordDict = ["pen", "pencil", "cil"]
    actual = Solution.wordBreak(Solution, s, wordDict)
    desired = []
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    s = "aaaaaa"
    wordDict = ["aaaa", "aa"]
    actual = Solution.wordBreak(Solution, s, wordDict)
    desired = [[0, 1], [1, 0], [1, 1, 1]]
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    s = "aaaaaaa"
    wordDict = ["aaaa", "aa"]
    actual = Solution.wordBreak(Solution, s, wordDict)
    desired = []
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()

    s = "ccacccbcab"
    wordDict = ["cc", "bb", "aa", "bc", "ac", "ca", "ba", "cb"]
    actual = Solution.wordBreak(Solution, s, wordDict)
    desired = []
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()



