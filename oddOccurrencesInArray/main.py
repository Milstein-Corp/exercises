# Definition for singly-linked list.
import math

def solution(A):
    A = sorted(A)
    n = int((len(A) - 1)/2)

    for i in range(0, n):
        if A[2*i] != A[2*i+1]:
            return A[2*i]

    return A[2*n]


if __name__ == '__main__':
    print("Test")
    A = [1, 3, 2, 3, 2, 1, 8]
    actual = solution(A)
    print("argument: %s" % (A))
    print("result: %s" % actual)
    print()

    print("Test")
    A = [1, 3, 2, 3, 2, 1, 8, 5, 5, 1, 1, 6, 7, 7, 6]
    actual = solution(A)
    print("argument: %s" % (A))
    print("result: %s" % actual)
    print()

    print("Test")
    A = [1]
    actual = solution(A)
    print("argument: %s" % (A))
    print("result: %s" % actual)
    print()

    print("Test")
    A = [3, 1, 3]
    actual = solution(A)
    print("argument: %s" % (A))
    print("result: %s" % actual)
    print()

