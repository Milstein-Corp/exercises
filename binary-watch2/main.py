class Solution(object):
    def readBinaryWatch(self, num):

        ans = [""]
        for i in range(0, 10):
            newans = []
            while ans:
                a = ans.pop()
                if a.count('1') < num: # and a[:4].count('1') < 3 and a[4:].count('1') < 5:
                    newans.append(a + '1')
                if a.count('0') < 10 - num:
                    newans.append(a + '0')
            ans = newans

        ans = sorted(ans, reverse=True)

        newans = []
        while ans:
            a = ans.pop()
            if int(a[:4], 2) < 12 and int(a[4:], 2) < 60:
                newans.append(str(int(a[:4], 2))+":"+str(int(a[4:], 2)).zfill(2))
        return newans


if __name__ == '__main__':
    input = 0
    desired = ["0:00"]
    actual = Solution.readBinaryWatch(Solution, input)
    print("input: %s" % input)
    print("desired: %s" % desired)
    print("acutal: %s" % actual)
    print()

    # input = 4
    # desired = ["00:00"]
    # actual = Solution.readBinaryWatch(Solution, input)
    # print("input: %s" % input)
    # print("desired: %s" % desired)
    # print("acutal: %s" % actual)
    # print()
