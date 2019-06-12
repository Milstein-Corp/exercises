# Definition for singly-linked list.
import math

def solution(A):


    return A[len(A)-1]


if __name__ == '__main__':
    print("CASE 1")
    A = [-1, -4, -8, -1, -10, -4, 1, 2, 3, 2]
    print("argument: %s" % (A))
    actual = solution(A)
    assert actual == 2
    print("result  : %s" % actual)
    print()

