# Definition for singly-linked list.
import math

def solution(A):
    if len(A) == 3:
        return A[0]*A[1]*A[2]

    A = sorted(A)
    poss = []
    negs =[]

    for a in A:
        if a >= 0:
            poss.append(a)
        else:
            negs.append(a)

    if not poss:
        print("case 1")
        return negs[-1]*negs[-2]*negs[-3]
    elif len(poss) == 1:
        print("case 2")
        return poss[0]*negs[0]*negs[1]
    elif len(poss) == 2:
        print("case 3")
        return poss[-1]*negs[0]*negs[1]
    elif len(poss) >= 3 and (len(negs) == 1 or len(negs) == 0):
        print("case 4")
        return poss[-1]*poss[-2]*poss[-3]
    elif len(poss) >= 3 and len(negs) > 1:
        print("case 5")
        return max(poss[-1]*poss[-2]*poss[-3], negs[0]*negs[1]*poss[-1])

    return 10


if __name__ == '__main__':
    print("CASE 1")
    A = [-1, -4, -8, -1, -10, -4]
    print("argument: %s" % (A))
    actual = solution(A)
    assert actual == -4
    print("result: %s" % actual)
    print()

    print("CASE 2")
    A = [3, -4, -8, -1, -10]
    print("argument: %s" % (A))
    actual = solution(A)
    print("result: %s" % actual)
    assert actual == 240
    print()

    print("CASE 3")
    A = [3, 4, -8, -2, -10]
    print("argument: %s" % (A))
    actual = solution(A)
    print("result: %s" % actual)
    assert actual == 320
    print()

    print("CASE 4")
    A = [3, 4, 5, 6]
    print("argument: %s" % (A))
    actual = solution(A)
    print("result: %s" % actual)
    assert actual == 120
    print()

    print("CASE 4")
    A = [3, 4, 5, 6, -8]
    print("argument: %s" % (A))
    actual = solution(A)
    print("result: %s" % actual)
    assert actual == 120
    print()

    print("CASE 5")
    A = [3, 4, 5, 6, -8, -10]
    print("argument: %s" % (A))
    actual = solution(A)
    print("result: %s" % actual)
    assert actual == 480
    print()

    print("CASE 5")
    A = [3, 4, 5, 6, -8, -10, -10]
    print("argument: %s" % (A))
    actual = solution(A)
    print("result: %s" % actual)
    assert actual == 600
    print()

    print("CASE R")
    A = [3, 4, 5, 6, -8, -10, -10, -10, 10]
    print("argument: %s" % (A))
    actual = solution(A)
    print("result: %s" % actual)
    assert actual == 1000
    print()

    print("CASE R")
    A = [3, 4, 5]
    print("argument: %s" % (A))
    actual = solution(A)
    print("result: %s" % actual)
    assert actual == 60
    print()

    print("CASE R")
    A = [3, 4, 5, 11, 11, -11, -11]
    print("argument: %s" % (A))
    actual = solution(A)
    print("result: %s" % actual)
    assert actual == 1331
    print()





