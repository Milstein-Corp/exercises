# Definition for singly-linked list.
import math


def solution(S):
    s = []

    for c in S:
        if c == "(":
            s.append(c)
        else:
            try:
                s.pop()
            except IndexError:
                return 0

    if len(s) == 0:
        return 1
    else:
        return 0


if __name__ == '__main__':
    A = ""
    print("argument: %s" % (A))
    actual = solution(A)
    print("result: %s" % actual)
    print()

    A = "(()))"
    print("argument: %s" % (A))
    actual = solution(A)
    print("result: %s" % actual)
    print()

    A = "((()))"
    print("argument: %s" % (A))
    actual = solution(A)
    print("result: %s" % actual)
    print()

    A = "((()))"
    print("argument: %s" % (A))
    actual = solution(A)
    print("result: %s" % actual)
    print()

    A = ")"
    print("argument: %s" % (A))
    actual = solution(A)
    print("result: %s" % actual)
    print()

    A = "("
    print("argument: %s" % (A))
    actual = solution(A)
    print("result: %s" % actual)
    print()

    A = "()()"
    print("argument: %s" % (A))
    actual = solution(A)
    print("result: %s" % actual)
    print()

    A = "()()(())"
    print("argument: %s" % (A))
    actual = solution(A)
    print("result: %s" % actual)
    print()

    A = "((((((("
    print("argument: %s" % (A))
    actual = solution(A)
    print("result: %s" % actual)
    print()

    A = ")))))))"
    print("argument: %s" % (A))
    actual = solution(A)
    print("result: %s" % actual)
    print()
