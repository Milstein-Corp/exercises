import string
from collections import defaultdict
import re

class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        d = defaultdict(lambda: 0)

        # paragraph_p = paragraph.split(" ")
        paragraph_p = re.split('\W+', paragraph)
        if len(paragraph_p) < 1:
            return ""

        for w in paragraph_p:
            w = w.lower()
            print(w)
            # print(w, end= " ||| ")
            # w = w.strip(string.punctuation).lower()
            # print(w)
            if w not in banned:
                d[w] += 1

        return sorted(d.items(), key=lambda x: (x[1], x[0]), reverse=True)[0][0]


if __name__ == '__main__':
    # It looks like str's maketrans function and string's translate method can be useful for quickly striping
    # "ball.".translate(str.maketrans('', '', string.punctuation))
    # https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    actual = Solution.mostCommonWord(Solution, paragraph, banned)
    desired = "ball"
    print("desired : " + str(desired))
    print("actual  : " + str(actual))
    assert actual == desired
    print()
    #
    # paragraph = "Bob hit a ball, the hit BALL flew far after it was hit. it it it;"
    # banned = ["hit"]
    # actual = Solution.mostCommonWord(Solution, paragraph, banned)
    # desired = "it"
    # print("desired : " + str(desired))
    # print("actual  : " + str(actual))
    # assert actual == desired
    # print()
    #
    # paragraph = "Bob hit a ball it it it;"
    # banned = ["hit", "it", "ball"]
    # actual = Solution.mostCommonWord(Solution, paragraph, banned)
    # desired = "bob"
    # print("desired : " + str(desired))
    # print("actual  : " + str(actual))
    # assert actual == desired
    # print()
    #
    # paragraph = "a, a, a, a, b,b,b,c, c"
    # banned = ["a"]
    # actual = Solution.mostCommonWord(Solution, paragraph, banned)
    # desired = "bob"
    # print("desired : " + str(desired))
    # print("actual  : " + str(actual))
    # assert actual == desired
    # print()



["a"]