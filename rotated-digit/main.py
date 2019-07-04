from collections import Counter

rotate_to = {"0": "0", "1": "1", "2": "5", "5": "2", "6": "9", "8": "8", "9": "6"}


class Solution(object):
    def rotate(self, x):

        x = list(reversed(str(x)))
        rotated = []

        for d in range(len(x)):
            try:
                rotated.append(rotate_to[x[d]])
            except KeyError:
                return -1

        return "".join(reversed(rotated))

    def rotatedDigits(self, N):
        k = self.rotate(self, 27)
        count = 0
        for i in range(1, N+1):
            rotated_digit = self.rotate(self, i)
            if rotated_digit != -1 and rotated_digit != str(i):
                count += 1

        return count


if __name__ == '__main__':
    N = 10
    desired = 4
    actual = Solution.rotatedDigits(Solution, N)
    print("N       : %s " % N)
    print("desired : %s " % desired)
    print("actual  : %s " % actual)
    assert desired == actual
    print()

    N = 5
    desired = 2
    actual = Solution.rotatedDigits(Solution, N)
    print("N       : %s " % N)
    print("desired : %s " % desired)
    print("actual  : %s " % actual)
    assert desired == actual
    print()

    N = 20
    desired = 9
    actual = Solution.rotatedDigits(Solution, N)
    print("N       : %s " % N)
    print("desired : %s " % desired)
    print("actual  : %s " % actual)
    assert desired == actual
    print()
