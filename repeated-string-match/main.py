class Solution(object):

    def repeatedStringMatch(self, A, B):
        repeats = -(-len(B)//len(A))

        for i in range(0, 2):
            if B in (i+repeats) * A:
                return i + repeats

        return -1

    def repeatedStrindgMatch_first_solution(self, A, B):
        repeated = A
        repeats = 1

        while len(repeated) < len(B):
            repeated += A
            repeats += 1

        sub = repeated.find(B)

        if sub != -1:
            return repeats

        repeated += A
        repeats += 1

        sub = repeated.find(B)

        if sub != -1:
            return repeats

        return -1


if __name__ == '__main__':
    A = "hell"
    B = "ellhellhell"
    desired = 3

    actual = Solution.repeatedStringMatch(Solution, A, B)
    print()
    print("argument : %s, %s" % (A, B))
    print("desired  : " + str(desired))
    print("actual   : " + str(actual))
    print()

    A = "helli"
    B = "ellhellhell"
    desired = -1

    actual = Solution.repeatedStringMatch(Solution, A, B)
    print()
    print("argument : %s, %s" % (A, B))
    print("desired  : " + str(desired))
    print("actual   : " + str(actual))
    print()

    A = "hel"
    B = "ellhellhell"
    desired = -1

    actual = Solution.repeatedStringMatch(Solution, A, B)
    print()
    print("argument : %s, %s" % (A, B))
    print("desired  : " + str(desired))
    print("actual   : " + str(actual))
    print()

    A = "hell"
    B = "ellheillhell"
    desired = -1

    actual = Solution.repeatedStringMatch(Solution, A, B)
    print()
    print("argument : %s, %s" % (A, B))
    print("desired  : " + str(desired))
    print("actual   : " + str(actual))
    print()


    A = "hell"
    B = "elhell"
    desired = -1

    actual = Solution.repeatedStringMatch(Solution, A, B)
    print()
    print("argument : %s, %s" % (A, B))
    print("desired  : " + str(desired))
    print("actual   : " + str(actual))
    print()

    A = "hell"
    B = "ellhell"
    desired = 2

    actual = Solution.repeatedStringMatch(Solution, A, B)
    print()
    print("argument : %s, %s" % (A, B))
    print("desired  : " + str(desired))
    print("actual   : " + str(actual))
    print()

    A = "abcd"
    B = "cdabcdab"
    desired = 3

    actual = Solution.repeatedStringMatch(Solution, A, B)
    print()
    print("argument : %s, %s" % (A, B))
    print("desired  : " + str(desired))
    print("actual   : " + str(actual))
    print()

