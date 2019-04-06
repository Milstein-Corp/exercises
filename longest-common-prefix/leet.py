class Solution:
    def shortestWord(self, strs) -> int:
        shortest = len(strs[0])
        for k in strs:
            if len(k) < shortest:
                shortest = len(k)
        return shortest

    def letter(self, strs, i) -> bool:
        same = True
        examin = strs[0][i]
        for k in strs:
            if (k[i] != examin):
                same = False
        return same

    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0:
            return ""
        short = self.shortestWord(self, strs)
        largestConsistentLetter = 0
        for l in range(short):
            con = self.letter(self, strs, l)

            if (con):
                largestConsistentLetter = l

        return strs[0][:largestConsistentLetter + 1]


if __name__ == "__main__":
    kk = ["stajj", "stadasdfaddd", "staove", "staephen", "staella", "staone"]
    output = Solution.longestCommonPrefix(Solution, kk)

    print(output)