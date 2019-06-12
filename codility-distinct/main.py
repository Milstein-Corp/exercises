# Definition for singly-linked list.
import math

def solution(A):
    if not A:
        return 0

    A = sorted(A)
    prev = A[0] + 1

    distinct = 0
    for a in A:
        if a != prev:
            distinct += 1
        prev = a

    return distinct


if __name__ == '__main__':
    A = [4, 1, 4]
    print("argument: %s" % (A))
    actual = solution(A)
    print("result: %s" % actual)
    print()

    A = [4, 1, 4, 1, 4, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1,\
         1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 4, 4, 4]
    print("argument: %s" % (A))
    actual = solution(A)
    print("result: %s" % actual)
    print()

    A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("argument: %s" % (A))
    actual = solution(A)
    print("result: %s" % actual)
    print()


