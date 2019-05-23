class Solution(object):
    def readBinaryWatch(self, num):
        times = [""]
        for i in range(10):
            newtimes = []
            while times:
                time = times.pop()
                if time.count("1") < num:
                    newtimes.append(time + "1")
                if time.count("0") < 10 - num:
                    newtimes.append(time + "0")
            times = newtimes

        times = [str(int(t[:4], 2)) + ":" + str(int(t[4:], 2)).zfill(2)
                 for t in sorted(times)
                     if int(t[:4], 2) < 12 and int(t[4:], 2) < 60]

        return times


if __name__ == '__main__':
    input = 3
    actual = Solution.readBinaryWatch(Solution, input)
    desired = [["7:00"], ["11:00"]]
    print("desired: %s" % desired)
    print("actual: %s" % actual)
    print()
