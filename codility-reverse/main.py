# Definition for singly-linked list.
import math

def solution(A):

    for i in range(len(A)//2):
        k = len(A)-1-i
        A[i], A[k] = A[k], A[i]

    return A

if __name__ == '__main__':
    print("Test")
    A = [1, 1, 1, 3, 2, 2, 2]
    print("argument: %s" % (A))
    solution(A)
    print("result: %s" % A)
    print()

    print("Test")
    A = [1, 1, 1, 2, 2, 2]
    print("argument: %s" % (A))
    solution(A)
    print("result: %s" % A)
    print()

