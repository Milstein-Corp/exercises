# Definition for singly-linked list.
import math

def solution(A, k):
    N = len(A)
    if N == 0:
        return []
    k = k % N

    front = A[N-k:N]
    back = A[0:N-k]

    return front + back

if __name__ == '__main__':
    print("Test")
    A = [1, 1, 3, 3, 3, 2, 2]
    k = 9
    print("argument: %s\nk: %s" % (A, k))
    actual = solution(A, k)
    print("result: %s" % actual)
    print()

    print("Test")
    A = [1, 1, 3, 3, 3, 2, 2]
    k = 2
    print("argument: %s\nk: %s" % (A, k))
    actual = solution(A, k)
    print("result: %s" % actual)
    print()

    print("Test")
    A = [1, 2]
    k = 1
    print("argument: %s\nk: %s" % (A, k))
    actual = solution(A, k)
    print("result: %s" % actual)
    print()

    print("Test")
    A = [1, 2]
    k = 2
    print("argument: %s\nk: %s" % (A, k))
    actual = solution(A, k)
    print("result: %s" % actual)
    print()

    print("Test")
    A = [1, 2]
    k = 3
    print("argument: %s\nk: %s" % (A, k))
    actual = solution(A, k)
    print("result: %s" % actual)
    print()

    print("Test")
    A = [1]
    k = 7
    print("argument: %s\nk: %s" % (A, k))
    actual = solution(A, k)
    print("result: %s" % actual)
    print()

    print("Test")
    A = []
    k = 7
    print("argument: %s\nk: %s" % (A, k))
    actual = solution(A, k)
    print("result: %s" % actual)
    print()



