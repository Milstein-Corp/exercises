class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = []
        for c in s:
            if c in ['(', '{', '[']:
                a.append(c)
            elif len(a) == 0:
                return False
            else:
                anti = a.pop()
                anabolic = self.flip(Solution, anti)
                if anabolic != c:
                    return False
        if len(a) != 0:
            return False

        return True

    def flip(self, character):
        """
        :rtype: string
        """
        if character == '(':
            character = ')'
        elif character == '{':
            character = '}'
        elif character == '[':
            character = ']'
        else:
            print("this case should never happen according to the problem statement")
        return character


if __name__ == '__main__':
    turn = Solution.isValid(Solution, "(((())))))")
    assert (turn == False)
    turn = Solution.isValid(Solution, "(((())))")
    print(turn)
    turn = Solution.isValid(Solution, "(((())")
    print(turn)
    turn = Solution.isValid(Solution, "({[]})")
    print(turn)
    turn = Solution.isValid(Solution, "")
    print(turn)
    turn = Solution.isValid(Solution, "(((())))))")
    print(turn)
    turn = Solution.isValid(Solution, "(((())))))")
    print(turn)
    turn = Solution.isValid(Solution, "(((())))))")
    print(turn)
