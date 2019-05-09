class Solution(object):
    def readBinaryWatch(self, num):
        if num == 0:
            return ["0:00"]

        a = ['0', '1']

        while len(a[0]) < 10:
            new = []
            for e in a:
                onecount = 0
                for k in e:
                    if k == '1': onecount += 1;
                zerocount = 0
                for k in e:
                    if k == '0': zerocount += 1;

                if zerocount < (10 - num):
                    new.append(e + '0')
                if onecount < num:
                    new.append(e + '1')
            a = new

        a = [e for e in a if int(e[0:4], 2) < 12 and int(e[4:], 2) < 59]

        hours = [str(int(e[0:4], 2)) for e in a]
        min = [str(int(e[4:], 2)).zfill(2) for e in a]

        ans = [h+":"+m for h, m in zip(hours, min)]
        return ans


if __name__ == '__main__':
    input = 4
    actual = Solution.readBinaryWatch(Solution, input)
    desired = ["0:01", "0:02", "0:04", "0:08", "0:16", "0:32", "1:00", "2:00", "4:00", "8:00"]
    print("desired: %s" % desired)
    print("actual : %s" % actual)
    print()
