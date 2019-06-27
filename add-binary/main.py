
class Solution(object):
    def addBinary(self, a, b):

        return bin(int(a, 2) + int(b, 2))[2:]


if __name__ == '__main__':
    a = "1010"
    b = "1011"
    desired = "10101"
    actual = Solution.addBinary(Solution, a, b)
    print("arguments: %s, %s" % (a, b))
    print("desired : " + str(desired))
    print("actual  : " + str(actual))
    print()
