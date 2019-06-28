class Solution(object):
    def addStringsForLoop(self, num1, num2):
        i = 0
        total = 0
        for i in range(len(num1)):
            total += 10**i * int(num1[-1-i])

        for i in range(len(num2)):
            total += 10**i * int(num2[-1-i])

        return str(total)

    def addStrings(self, num1, num2):
        i = 0
        total = 0

        while i < len(num1):
            total += 10**i * int(num1[-1-i])
            i += 1

        i = 0
        while i < len(num2):
            total += 10**i * int(num2[-1-i])
            i += 1

        return str(total)

if __name__ == '__main__':
    num1 = "343"
    num2 = "4"
    desired = "347"
    actual = Solution.addStrings(Solution, num1, num2)
    print("arguments: %s,%s" % (num1, num2))
    print("desired : " + str(desired))
    print("actual  : " + str(actual))
    # assert desired == actual
    print()

