def checkInclusion(s1, s2):
    windowSize = len(s1)
    for c in range(0, len(s2)-windowSize+1):
        for i in range(windowSize):
            print(c + i, end=", ")
        print()


    print("last index: %s" % str(len(s2)-1))


    return False

if __name__ == '__main__':
    substring = "abc"
    longstring = "eidbaoooo"
    desired = True
    actual = checkInclusion(substring, longstring)
    print()
    print("sub, long : %s, %s" % (substring, longstring))
    print("desired: %s" % desired)
    print("actual : %s" % actual)
    print()


    # substring = "ab"
    # longstring = "eidboaoooo"
    # desired = False
    # actual = checkInclusion(substring, longstring)
    # print()
    # print("sub, long : %s, %s" % (substring, longstring))
    # print("desired: %s" % desired)
    # print("actual : %s" % actual)
    # print()
    #
    # substring = "ei"
    # longstring = "eidboaoooo"
    # desired = True
    # actual = checkInclusion(substring, longstring)
    # print()
    # print("sub, long : %s, %s" % (substring, longstring))
    # print("desired: %s" % desired)
    # print("actual : %s" % actual)
    # print()
    #
    # substring = "oj"
    # longstring = "eidboaooooj"
    # desired = True
    # actual = checkInclusion(substring, longstring)
    # print()
    # print("sub, long : %s, %s" % (substring, longstring))
    # print("desired: %s" % desired)
    # print("actual : %s" % actual)
    # print()
    #
    # substring = "aaa"
    # longstring = "eidboaaaaooooj"
    # desired = True
    # actual = checkInclusion(substring, longstring)
    # print()
    # print("sub, long : %s, %s" % (substring, longstring))
    # print("desired: %s" % desired)
    # print("actual : %s" % actual)
    # print()
#
#