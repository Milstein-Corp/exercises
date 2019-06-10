# Definition for singly-linked list.
import math

def solution(C, k):
    dp = [0] + k*[math.inf]

    for nc in C:
        for target in range(nc, k+1):
            dp[target] = min(dp[target], dp[target-nc] + 1)

    # dp[target] is the number of coins required to
    # add up to target. The index for the array
    # I was building ended up having some meaning.
    # It was the total that all the coins added up to.
    # I had an array of minimum number of coins to add up
    # to the zero index of that element. Element = num coins.
    # zero index = value they add up to. When I have a new coin,
    # I visit elements according to their zero index, not there value.
    # Which elements in the array do I want to visit? Those whose
    # 'value they add up to' (zero index) is equal to or larger than
    # the new coin that I am examining.
    # The targets happen to be a good condidate for indices. They start
    # at zero, and go up in ones to the desired value. This is part of the
    # idea. I will find how many coins I can use to add up to lesser values
    # than the final target value. And the number of coins? That will be
    # the Value. index -> target, number of coins -> value. And I will fill
    # that array in for having no coins, And then, with each new coin, I will
    # update the array. Yes, the targets start at zero, this is apparently
    # useful once you see that target-nc appears as an index - you need
    # this to return a zero, because 1 will be added, and that will be the
    # only coin you need. In other words, as you build your array, you look back
    # to the element s.t. element_val + nc = target, and element value needs to be
    # zero. So if you want that first '1' in the row for a new coin to be handled
    # correctly, then you need to have the answer stored for the number of coins to
    # add up to zero, just like you have the number of coins to add up to other values

    return dp[k]


if __name__ == '__main__':
    print("Test")
    C = [1, 3, 2]
    k = 6
    actual = solution(C, k)
    print("argument: %s \ntarget: %s" % (C, k))
    print("header: %s" % list(range(k+1)))
    print("result: %s" % actual)
    print()

    print("Test")
    C = [3, 6, 2, 1]
    k = 6
    actual = solution(C, k)
    print("argument: %s \ntarget: %s" % (C, k))
    print("header: %s" % list(range(k+1)))
    print("result: %s" % actual)
    print()

    print("Test")
    C = [6]
    k = 12
    actual = solution(C, k)
    print("argument: %s \ntarget: %s" % (C, k))
    print("header: %s" % list(range(k+1)))
    print("result: %s" % actual)
    print()


