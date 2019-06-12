from operator import itemgetter


def solution(N, S):
    seats = S.split(" ")
    if len(seats) == 1 and seats[0] == '':
        seats = []
    # seats is either empty or has valid seat numbers as entries

    total = 0
    for r in range(N, 0, -1):
        if (str(r) + "A" not in seats) and \
                (str(r) + "B" not in seats) and \
                (str(r) + "C" not in seats):
            total += 1

        if (str(r) + "H" not in seats) and \
                (str(r) + "J" not in seats) and \
                (str(r) + "K" not in seats):
            total += 1

        if (str(r) + "D" not in seats) and \
                (str(r) + "E" not in seats) and \
                (str(r) + "F" not in seats):
            total += 1
        elif (str(r) + "E" not in seats) and \
                (str(r) + "F" not in seats) and \
                (str(r) + "G" not in seats):
            total += 1

    return total


if __name__ == '__main__':
    print("CASE 1")
    N = 3
    S = "1K 2A 3K 2D 3A 3B"
    print("N: %s ---- S: %s" % (N, S))
    actual = solution(N, S)
    assert actual == 5
    print("result  : %s" % actual)
    print()

    print("CASE 2")
    N = 3
    S = ""
    print("N: %s ---- S: %s" % (N, S))
    actual = solution(N, S)
    assert actual == 9
    print("result  : %s" % actual)
    print()

    print("CASE 3")
    N = 1
    S = ""
    print("N: %s ---- S: %s" % (N, S))
    actual = solution(N, S)
    assert actual == 3
    print("result  : %s" % actual)
    print()

    print("CASE 4")
    N = 50
    S = ""
    print("N: %s ---- S: %s" % (N, S))
    actual = solution(N, S)
    assert actual == 150
    print("result  : %s" % actual)
    print()

    print("CASE 5")
    N = 5
    S = "1A 5K 3D"
    print("N: %s ---- S: %s" % (N, S))
    actual = solution(N, S)
    assert actual == 13
    print("result  : %s" % actual)
    print()

    print("CASE 6")
    N = 5
    S = "1A"
    print("N: %s ---- S: %s" % (N, S))
    actual = solution(N, S)
    assert actual == 14
    print("result  : %s" % actual)
    print()

    print("CASE 6")
    N = 5
    S = "1A 1D 2D 3G 4G 5D"
    print("N: %s ---- S: %s" % (N, S))
    actual = solution(N, S)
    assert actual == 14
    print("result  : %s" % actual)
    print()

    print("CASE 7")
    N = 5
    S = "1A 1D 2D 3G 4G 5D 5G 1G"
    print("N: %s ---- S: %s" % (N, S))
    actual = solution(N, S)
    assert actual == 12
    print("result  : %s" % actual)
    print()

    print("CASE 8")
    N = 1
    S = "1A 1D 1D 1G 1G 1D 1G 1G 1B 1K"
    print("N: %s ---- S: %s" % (N, S))
    actual = solution(N, S)
    print("result  : %s" % actual)
    assert actual == 0
    print()

    print("CASE 9")
    N = 2
    S = "1A 1D 1D 1G 1G 1D 1G 1G 1B 1K" + " 2A 2D 2D 2G 2G 2D 2G 2G 2B 2K"
    print("N: %s ---- S: %s" % (N, S))
    actual = solution(N, S)
    print("result  : %s" % actual)
    assert actual == 0
    print()

    biglist = []
    for i in range(1, 51):
        one = [str(i) + x for x in ["A", "B"]]
        biglist += one
    biglist = " ".join(biglist)
    print("CASE 10")
    N = 50
    S = biglist
    print("N: %s ---- S: %s" % (N, S))
    actual = solution(N, S)
    print("result  : %s" % actual)
    assert actual == 100
    print()

    biglist = []
    for i in range(1, 51):
        one = [str(i) + x for x in ["A", "B", "K"]]
        biglist += one
    biglist.reverse()
    biglist = " ".join(biglist)
    print("CASE 11")
    N = 50
    S = biglist
    print("N: %s ---- S: %s" % (N, S))
    actual = solution(N, S)
    print("result  : %s" % actual)
    assert actual == 50
    print()
