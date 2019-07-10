import string
from collections import defaultdict
import re

class Solution(object):

    def write(self, curr, count, write, chars):
        """
        write curr and count to position write in chars

        :param curr:
        :param count:
        :param write:
        :param chars:
        :return: updated write, chars
        """
        chars[write] = curr
        write += 1
        if count != 1:
            start = write
            for d in range(len(str(count))):
                chars[start + d] = str(count)[d]
                write += 1
        return write, chars

    def compress(self, chars):
        if len(chars) == 1:
            return 1

        write = 0
        curr = chars[0]
        count = 1
        examine = 1

        while examine < len(chars):
            if chars[examine] == curr:
                count += 1
                examine += 1
            else:
                write, chars = self.write(self, curr, count, write, chars)
                curr = chars[examine]
                count = 1
                examine += 1

        write, chars = self.write(self, curr, count, write, chars)

        return write




# class Solution(object):
#     def compress(self, chars):
#         anchor = write = 0
#         for read, c in enumerate(chars):
#             if read + 1 == len(chars) or chars[read + 1] != c:
#                 chars[write] = chars[anchor]
#                 write += 1
#                 if read > anchor:
#                     for digit in str(read - anchor + 1):
#                         chars[write] = digit
#                         write += 1
#                 anchor = read + 1
#         return write


# class Solution(object):
#     def compress(self, chars):
#         if len(chars) < 1:
#             return 0
#
#         location = 0
#         letter = chars[0]
#         count = 1
#         i = 1  # i is unvisited
#         write = 0  # 0, 2, 4, 6
#         chars[write] = letter  # letter is written to write
#
#         i = 1
#         while i < len(chars):
#             'i' is unvisited, 'count' is the count of 'letter' thus far
#             'write' is the last place we wrote to in the array
#             'letter' is written to 'write'
#             'original' is where we found letter
#             'original' can come along ways after write
#             if chars[i] == letter:
#                 count += 1
#                 i += 1
#             else:
#                 chars[write + 1], letter, count, location = str(count), chars[i], 1, i
#                 write += 1
#                 i += 1

        # if write + 1 is off the list
        # if write + 1 >= len(chars):
        #     chars.append(count)
        #
        # return chars


if __name__ == '__main__':
    # It looks like str's maketrans function and string's translate method can be useful for quickly striping
    # "ball.".translate(str.maketrans('', '', string.punctuation))
    # https://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string
    foam = ["a", "a", "a", "a", "a", "a", "a"]
    print("argument: " + str(foam))
    actual = Solution.compress(Solution, foam)
    print("argument: " + str(foam))
    print("actual  : " + str(actual))
    print()


    foam = ["a", "a", "a", "a", "a", "a", "a", "b", "c", "d", "e", "f", "g"]
    print("argument: " + str(foam))
    actual = Solution.compress(Solution, foam)
    print("argument: " + str(foam))
    print("actual  : " + str(actual))
    print()


    foam = ["a", "a", "a", "b", "c", "d", "e", "e", "f", "g", "g", "g", "g"]
    print("argument: " + str(foam))
    actual = Solution.compress(Solution, foam)
    print("argument: " + str(foam))
    print("actual  : " + str(actual))
    print()