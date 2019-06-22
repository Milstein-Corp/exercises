# Definition for singly-linked list.

def exam(x):
    a = x.split(" ")
    identifier = a[0]
    firstentry = a[1]

    if firstentry.isdigit():
        metric = tuple([True])
    else:
        # metric = (False, len(a)) + tuple(a[1:]) + tuple(identifier)
        metric = (False, len(a), a[1:]) + tuple(identifier)
        print(metric)

    return metric


class Solution(object):
    def reorderLogFiles(self, lf):
        lf.sort(key=exam)
        return lf


if __name__ == '__main__':
    logFiles = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
    actual = Solution.reorderLogFiles(Solution, logFiles.copy())
    desired = ["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"]
    print("logFiles: " + str(logFiles))
    print("desired : " + str(desired))
    print("actual  : " + str(actual))
    assert actual == desired
    print()

    # a = ["mo"]
    # b = ["mz"]
    # print(str(a) + "<" + str(b) + ": " + str(a<b))
    #
    # a = ["ma"]
    # b = ["mo"]
    # print(str(a) + "<" + str(b) + ": " + str(a<b))
    #
    # a = ["mo"]
    # b = ["mo", "a"]
    # print(str(a) + "<" + str(b) + ": " + str(a<b))
    #
    # a = ["m", "w"]
    # b = ["mo"]
    # print(str(a) + "<" + str(b) + ": " + str(a<b))

