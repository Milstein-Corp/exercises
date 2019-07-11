from collections import deque

class Solution(object):
    def longestOnes(self, A, K):

        # q = queue.Queue(K+1)
        zeros = deque()

        maxLength = 0
        for i, a in enumerate(A):
            if a == 0:
                if len(zeros) < K + 1:
                    zeros.append(i)
                else:
                    zeros.popleft()
                    zeros.append(i)
            # The location of the last K + 1 zeros is known
            # print("i, a, zeros: %s, %s, %s" % (i, a, list(zeros)))
            if len(zeros) == K + 1:
                bestStart = zeros[0] + 1
            else:
                bestStart = 0
            # print("length: %s " % int(i - bestStart + 1))
            maxLength = max(maxLength, i - bestStart + 1)

        return maxLength


if __name__ == '__main__':
    A = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
    K = 2
    desired = 6
    actual = Solution.longestOnes(Solution, A, K)
    print()
    print("argument : %s, %s" % (A, K))
    print("desired  : %s " % desired)
    print("actual   : " + str(actual))
    print()

    A = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1]
    K = 2
    desired = 7
    actual = Solution.longestOnes(Solution, A, K)
    print()
    print("argument : %s, %s" % (A, K))
    print("desired  : %s " % desired)
    print("actual   : " + str(actual))
    print()

    A = [1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1]
    K = 2
    desired = 11
    actual = Solution.longestOnes(Solution, A, K)
    print()
    print("argument : %s, %s" % (A, K))
    print("desired  : %s " % desired)
    print("actual   : " + str(actual))
    print()

    A = [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1]
    K = 2
    desired = 9
    actual = Solution.longestOnes(Solution, A, K)
    print()
    print("argument : %s, %s" % (A, K))
    print("desired  : %s " % desired)
    print("actual   : " + str(actual))
    print()

    A = [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1]
    K = 0
    desired = 3
    actual = Solution.longestOnes(Solution, A, K)
    print()
    print("argument : %s, %s" % (A, K))
    print("desired  : %s " % desired)
    print("actual   : " + str(actual))
    print()
