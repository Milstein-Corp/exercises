import string
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

    def canConstruct_second_solution(self, ransomNote, magazine):
        magazine_counts = Counter(magazine)
        ransomNote_counts = Counter(ransomNote)

        for i in ransomNote_counts:
            if ransomNote_counts[i] > magazine_counts[i]:
                return False

        return True

    def canConstruct_first_solution(self, ransomNote, magazine):
        for l in string.ascii_lowercase:
            if ransomNote.count(l) > magazine.count(l):
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