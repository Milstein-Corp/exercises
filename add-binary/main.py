class Solution(object):
    def addBinary(self, a, b):
        a = a[::-1]
        b = b[::-1]

        if len(a) < len(b):
            a, b = b, a

        ans = []

        carry = 0
        last_index = -1
        for i in range(len(b)):
            if a[i] == "1" and b[i] == "1":
                if carry:
                    ans.append("1")
                    carry = 1
                else:
                    ans.append("0")
                    carry = 1
            elif a[i] == "1" or b[i] == "1":
                if carry:
                    ans.append("0")
                    carry = 1
                else:
                    ans.append("1")
                    carry = 0
            else:
                if carry:
                    ans.append("1")
                    carry = 0
                else:
                    ans.append("0")
                    carry = 0
            last_index = i

        last_index += 1

        while last_index < len(a):
            if carry == 1 and a[last_index] == "1":
                ans.append("0")
                carry = 1
            elif carry == 0 and a[last_index] == "1":
                ans.append("1")
                carry = 0
            elif carry == 1 and a[last_index] == "0":
                ans.append("1")
                carry = 0
            elif carry == 0 and a[last_index] == "0":
                ans.append("0")
                carry = 0
            last_index += 1

        if carry:
            ans.append("1")

        return "".join(ans[::-1])


if __name__ == '__main__':
    a = "1010"
    b = "1011"
    desired = "10101"
    actual = Solution.addBinary(Solution, a, b)
    print("arguments: %s, %s" % (a, b))
    print("desired : " + str(desired))
    print("actual  : " + str(actual))
    print()

    a = "10101"
    b  = "1011"
    desired = "100000"
    actual = Solution.addBinary(Solution, a, b)
    print("arguments: %s, %s" % (a, b))
    print("desired : " + str(desired))
    print("actual  : " + str(actual))
    print()

    a = "1"
    b = "1"
    desired = "10"
    actual = Solution.addBinary(Solution, a, b)
    print("arguments: %s, %s" % (a, b))
    print("desired : " + str(desired))
    print("actual  : " + str(actual))
    print()

    a = "0"
    b = "1"
    desired = "1"
    actual = Solution.addBinary(Solution, a, b)
    print("arguments: %s, %s" % (a, b))
    print("desired : " + str(desired))
    print("actual  : " + str(actual))
    print()
