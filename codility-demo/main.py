# Definition for singly-linked list.
def printl(l, header):
    cur = l
    print(header, end=": ")
    while cur:
        print(cur.val, end=", ")
        cur = cur.next
    print()


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None



def solution(A):
    parr = sorted(A)
    clean = [-1]
    for k in parr:
        if k > 0 and k != clean[-1]:
            clean.append(k)
    clean = clean[1:] + [-1]
    i = 1
    for e in clean:
        if i != e:
            return i
        i += 1

    return len(parr)


if __name__ == '__main__':
    print("Test")
    arr = [1, 3, 2, -1]
    actual = solution(arr)
    print("argument: %s " % arr)
    print("actual: %s" % actual)
    print()

    print("Test")
    arr = [1, 3, 2, 7, -8]
    actual = solution(arr)
    print("argument: %s " % arr)
    print("actual: %s" % actual)
    print()

    print("Test")
    arr = []
    actual = solution(arr)
    print("argument: %s " % arr)
    print("actual: %s" % actual)
    print()

    print("Test")
    arr = [2, 3, 4, 5, 6, 7]
    actual = solution(arr)
    print("argument: %s " % arr)
    print("actual: %s" % actual)
    print()

    print("Test")
    arr = [1, 2, 4, 5, 6, 2, 2, 2, 2, -1, -2, -4]
    actual = solution(arr)
    print("argument: %s " % arr)
    print("actual: %s" % actual)
    print()



