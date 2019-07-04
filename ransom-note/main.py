from collections import Counter


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        letters = {}

        for c in magazine:
            try:
                letters[c] += 1
            except:  # This is equivalent to a default dict now.
                letters[c] = 1

        for c in ransomNote:
            try:
                letters[c] -= 1
                if letters[c] < 0:
                    return False
            except:
                return False

        return True


if __name__ == '__main__':
    magazine = "rbbbbaaaaccezq"
    ransomNote = "aaaq"
    desired = True
    actual = Solution.canConstruct(Solution, ransomNote, magazine)
    print("magazine: %s " % magazine)
    print("note    : %s " % ransomNote)
    print("desired : " + str(desired))
    print("actual  : " + str(actual))
    assert desired == actual
    print()

    magazine = "aaaa"
    ransomNote = "aaaa"
    desired = True
    actual = Solution.canConstruct(Solution, ransomNote, magazine)
    print("magazine: %s " % magazine)
    print("note    : %s " % ransomNote)
    print("desired : " + str(desired))
    print("actual  : " + str(actual))
    assert desired == actual
    print()

    magazine = "aaaa"
    ransomNote = "aaaaa"
    desired = False
    actual = Solution.canConstruct(Solution, ransomNote, magazine)
    print("magazine: %s " % magazine)
    print("note    : %s " % ransomNote)
    print("desired : " + str(desired))
    print("actual  : " + str(actual))
    assert desired == actual
    print()

    magazine = "aaaaaasdhjkfaksjdhfaskdhjf"
    ransomNote = "aaaaa"
    desired = True
    actual = Solution.canConstruct(Solution, ransomNote, magazine)
    print("magazine: %s " % magazine)
    print("note    : %s " % ransomNote)
    print("desired : " + str(desired))
    print("actual  : " + str(actual))
    assert desired == actual
    print()
#