class Solution(object):

    def toLowerCaseArray(self, str):

        p = 0
        ans = []

        while p < len(str):
            if 65 <= ord(str[p]) <= 90:
                lower = chr(ord(str[p])+32)
            else:
                lower = str[p]
            ans.append(lower)
            p += 1

        return "".join(ans)


    def toLowerCase(self, str):

        p = 0
        ans = ""

        while p < len(str):
            if 65 <= ord(str[p]) <= 90:
                lower = chr(ord(str[p])+32)
            else:
                lower = str[p]
            ans += lower
            p += 1

        return "".join(ans)

if __name__ == '__main__':
    foam = "Hello World"
    desired = "hello world"
    print("argument : " + str(foam))
    actual = Solution.toLowerCase(Solution, foam)
    print("desired  : " + str(desired))
    print("actual   : " + str(actual))
    print()

    foam = "HELLO WoRld"
    desired = "hello world"
    print("argument : " + str(foam))
    actual = Solution.toLowerCase(Solution, foam)
    print("desired  : " + str(desired))
    print("actual   : " + str(actual))
    print()

    foam = "HE#LLO WoRld!!!"
    desired = "he#llo world!!!"
    print("argument : " + str(foam))
    actual = Solution.toLowerCase(Solution, foam)
    print("desired  : " + str(desired))
    print("actual   : " + str(actual))
    print()