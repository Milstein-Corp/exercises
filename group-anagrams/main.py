from collections import Counter


class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = {}
        for w in strs:
            key = "".join(sorted(w))
            try:
                anagrams[key].append(w)
            except:
                anagrams[key] = [w]

        ans = []
        for k, group in anagrams.items():
            ans.append(group)
        return ans

    def groupAnagrams_first_solution(self, strs):
        anagrams = {}

        for w in strs:
            key_gen = Counter(w)
            key = ""
            for l, c in sorted(key_gen.items()):
                key = key + l + str(c)

            try:
                anagrams[key].append(w)
            except:
                anagrams[key] = [w]

        ans = []
        for k, group in anagrams.items():
            ans.append(group)

        return ans


if __name__ == '__main__':
    s = ["eat", "tea", "tan", "ate", "nat", "bat"]
    actual = Solution.groupAnagrams(Solution, s)
    print()
    print("argument : %s" % s)
    print("actual   : " + str(actual))
    print()
