from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        magazine_counts = Counter(magazine)
        ransomNote_counts = Counter(ransomNote)

        for i in ransomNote_counts:
            if ransomNote_counts[i] > magazine_counts[i]:
                return False

        return True


if __name__ == '__main__':
    magazine = "bbbbaaaaccezq"
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