import string
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        for l in string.ascii_lowercase:
            if ransomNote.count(l) > magazine.count(l):
                return False

        return True


if __name__ == '__main__':
    ransomNote = "aaa"
    magazine = "aaaa"
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

