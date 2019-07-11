def checkInclusion(s1, s2):
    windowSize = len(s1)
    substring = {}
    parent = {}

    for c in s1[0:windowSize]:
        try:
            substring[c] += 1
        except:
            substring[c] = 1

    for c in s2[0:windowSize]:
        try:
            parent[c] += 1
        except:
            parent[c] = 1

    if parent == substring:
        return True

    for c in range(1, len(s2)-windowSize+1):
        if parent[s2[c-1]] == 1:
            del parent[s2[c-1]]
        else:
            parent[s2[c - 1]] -= 1

        try:
            parent[s2[c+windowSize-1]] += 1
        except KeyError:
            parent[s2[c+windowSize-1]] = 1

        # print("parent c: %s" % c)
        # print(parent)
        # print(substring)


        if parent == substring:
            return True

        # for i in range(windowSize):
        #     print(c + i, end=", ")
        # print()
        # print()


    # print("last index: %s" % str(len(s2)-1))


    return False

if __name__ == '__main__':
    substring = "ab"
    longstring = "eidbaoooo"
    desired = True
    actual = checkInclusion(substring, longstring)
    print()
    print("sub, long : %s, %s" % (substring, longstring))
    print("desired: %s" % desired)
    print("actual : %s" % actual)
    print()


    substring = "ab"
    longstring = "eidboaoooo"
    desired = False
    actual = checkInclusion(substring, longstring)
    print()
    print("sub, long : %s, %s" % (substring, longstring))
    print("desired: %s" % desired)
    print("actual : %s" % actual)
    print()

    substring = "ei"
    longstring = "eidboaoooo"
    desired = True
    actual = checkInclusion(substring, longstring)
    print()
    print("sub, long : %s, %s" % (substring, longstring))
    print("desired: %s" % desired)
    print("actual : %s" % actual)
    print()

    substring = "oj"
    longstring = "eidboaooooj"
    desired = True
    actual = checkInclusion(substring, longstring)
    print()
    print("sub, long : %s, %s" % (substring, longstring))
    print("desired: %s" % desired)
    print("actual : %s" % actual)
    print()

    substring = "aaa"
    longstring = "eidboaaaaooooj"
    desired = True
    actual = checkInclusion(substring, longstring)
    print()
    print("sub, long : %s, %s" % (substring, longstring))
    print("desired: %s" % desired)
    print("actual : %s" % actual)
    print()

#