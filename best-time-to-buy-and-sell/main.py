def maxProfit(prices):
    if not prices:
        return 0

    best_profit = 0
    cheapest = p[0]

    for p in prices[1:]:
        if p < cheapest:
            cheapest = p

        profit = p - cheapest

        if profit > best_profit:
            best_profit = profit


    return profit

if __name__ == '__main__':
    # input = [1, 2, 3, 4, 5, 6]
    # profit = maxProfit(input)
    # print("correct: %s" % 5)
    # print("actual : %s" % profit)



    tot = "abcb"

    print(tot.replace("b", "", 3))




