# Definition for singly-linked list.
import math


def solution(A):
    if len(A) < 2:
        return 0

    start = [0]*len(A)
    end = [0]*len(A)

    for pos in range(len(A)):
        if pos - A[pos] <= 0:
            start[0] += 1
        else:
            start[pos-A[pos]] += 1

        if pos + A[pos] >= len(A) - 1:
            end[len(A)-1] += 1
        else:
            end[pos+A[pos]] += 1

    total = 0
    openc = 0
    for pos in range(len(A)):
        total += start[pos] * (start[pos] - 1)/2
        total += openc * start[pos]
        openc = openc + start[pos] - end[pos]

    return int(total)


if __name__ == '__main__':
    A = [4, 1, 4]
    print("argument: %s" % (A))
    actual = solution(A)
    print("result: %s" % actual)
    print()

    A = [4, 1, 1, 1, 4]
    print("argument: %s" % (A))
    actual = solution(A)
    print("result: %s" % actual)
    print()

    A = [1, 1]
    print("argument: %s" % (A))
    actual = solution(A)
    print("result: %s" % actual)
    print()

    A = [1, 0, 0, 1, 0, 0, 0, 1]
    print("argument: %s" % (A))
    actual = solution(A)
    print("result: %s" % actual)
    print()

