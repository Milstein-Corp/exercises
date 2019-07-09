class Solution(object):
    def countAndSay(self, n): # my way. The slow way
        if n < 1:
            return ""

        # i and val are tied.
        i = 1  # ith term in the sequence
        val = "1"  # value at the ith term

        while i < n:
            i += 1  # increment i

            print("************* " + str(i) + " *************")
            print("destination: " + str(i))
            print("start: " + str(val))
            print()
            # increment val
            ans = []
            see = val[0]
            count = 1  # bug
            j = 0

            print("j  : %s " % j)
            print("ans: %s " % ans)
            print("see: %s " % see)
            print("cou: %s " % count)

            print("----------------------")

            for j in range(1, len(val)):
                if val[j] == see:
                    ans, see, count = ans, see, count + 1
                else:
                    see, count, ans = val[j], 1, ans + [str(count), str(see)]
                print("j  : %s " % j)
                print("ans: %s " % ans)
                print("see: %s " % see)
                print("cou: %s " % count)

                print("----------------------")



            ans.append(str(count))
            ans.append(str(see))
            see = None
            count = None
            j = j + 1
            print("j  : %s " % j)
            print("ans: %s " % ans)
            print("see: %s " % see)
            print("cou: %s " % count)

            print("----------------------")

            val = "".join(ans)

        print()
        print("conclude function")
        print()
        return val


    def countAndSay_solution(self, n): # The fast way
        result = '1'
        for _ in range(n-1):
            prev = result
            result = ''
            j = 0
            while j < len(prev):
                cur = prev[j]
                cnt = 1
                j += 1
                while j < len(prev) and prev[j] == cur:
                    cnt += 1
                    j += 1
                result += str(cnt) + str(cur)
        return result


if __name__ == '__main__':
    n = 4
    desired = "1211"
    actual = Solution.countAndSay(Solution, n)
    print("argument: %s" % n)
    print("desired : " + str(desired))
    print("actual  : " + str(actual))
    assert desired == actual
    print()
