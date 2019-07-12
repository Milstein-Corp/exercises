from collections import Counter

class Solution:
    def numJewelsInStones_first(self, J, S):
        count = 0
        for c in S:
            if c in J:
                count += 1
        return count

    def numJewelsInStones_second(self, J, S):
        count = 0

        jewels = set(J)

        for c in S:
            if c in jewels:
                count += 1

        return count

    def numJewelsInStones(self, J, S):
        count = 0

        stones = Counter(S)
        for j in J:
            count += stones[j]

        return count


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == '__main__':
    S = "aaabbbccc"
    J = "a"
    answer = 3
    actual = Solution.numJewelsInStones(Solution, J, S)
    print("answer: %s" % answer)
    print("actual: %s" % actual)
    print()

    S = "aaabbccc"
    J = "b"
    answer = 2
    actual = Solution.numJewelsInStones(Solution, J, S)
    print("answer: %s" % answer)
    print("actual: %s" % actual)

