class Solution(object):
    def intersection(self, arr1, arr2):
        arr1.sort()
        arr2.sort()

        if not arr1:
            return None

        if not arr2:
            return None

        outer = 0
        inner = 0

        intersection = set()
        while outer < len(arr1):
            while inner < len(arr2) - 1 and arr2[inner] < arr1[outer]:
                inner += 1

            print(inner)
            if arr1[outer] == arr2[inner]:
                intersection.add(arr1[outer])
                # inner += 1
            outer += 1

        return list(intersection)


if __name__ == '__main__':
    arr1 = [1, 2, 2, 1]
    arr2 = [1, 2]
    actual = Solution.intersection(Solution, arr1.copy(), arr2.copy())
    desired = [1, 2]
    print("arr1, arr2: %s %s " % (arr1, arr2))
    print("desired : " + str(desired))
    print("actual  : " + str(actual))
    assert actual == desired
    print()

    arr1 = [1, 2, 2, 1]
    arr2 = [4, 2]
    actual = Solution.intersection(Solution, arr1.copy(), arr2.copy())
    desired = [2]
    print("arr1, arr2: %s %s " % (arr1, arr2))
    print("desired : " + str(desired))
    print("actual  : " + str(actual))
    assert actual == desired
    print()

    arr1 = [1, 2, 2, 1, 1, 2, 2, 3, 4, 5, 6]
    arr2 = [4, 2, 6, 10]
    actual = Solution.intersection(Solution, arr1.copy(), arr2.copy())
    desired = [2, 4, 6]
    print("arr1, arr2: %s %s " % (arr1, arr2))
    print("desired : " + str(desired))
    print("actual  : " + str(actual))
    assert actual == desired
    print()

    arr1 = [1, 2, 2, 1, 1, 2, 2, 3, 4, 5, 6]
    arr2 = []
    actual = Solution.intersection(Solution, arr1.copy(), arr2.copy())
    desired = None
    print("arr1, arr2: %s %s " % (arr1, arr2))
    print("desired : " + str(desired))
    print("actual  : " + str(actual))
    assert actual == desired
    print()

    arr1 = [1, 2, 2, 1, 1, 2, 2, 3, 4, 5, 6]
    arr2 = [1]
    actual = Solution.intersection(Solution, arr1.copy(), arr2.copy())
    desired = [1]
    print("arr1, arr2: %s %s " % (arr1, arr2))
    print("desired : " + str(desired))
    print("actual  : " + str(actual))
    assert actual == desired
    print()

    arr1 = [1]
    arr2 = [1, 2, 2, 1, 1, 2, 2, 3, 4, 5, 6]
    actual = Solution.intersection(Solution, arr1.copy(), arr2.copy())
    desired = [1]
    print("arr1, arr2: %s %s " % (arr1, arr2))
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
