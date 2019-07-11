def checkInclusion(s1, s2):

    s1 = sorted(s1)
    front = 0
    interval = len(s1) - 1
    back = front + interval

    for c in range(len(s2)-interval):

        # print(c)
        # print(c + interval + 1)
        b = sorted(s2[c:c + interval + 1])
        # print(b)
        # print(s1)
        # print()
        if s1 == b:
            return True


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

