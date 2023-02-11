def solution(lotteries):

    max_percent = 0
    win_price = []

    for idx, lottery in enumerate(lotteries):
        winner, candidate, price = lottery
        now_percent = winner / (candidate + 1) if winner <= candidate else 1 # +1 은 본인 자신, 당첨자가 산 사람보다 많으면 무조건 1

        if now_percent > max_percent:
            max_percent = now_percent
            win_price = [(price, idx)]

        elif now_percent == max_percent:
            win_price.append((price, idx))

    win_price.sort(reverse = True)

    return win_price[0][1] + 1


lotteries = [[10, 19, 800], [20, 39, 200], [100, 199, 500]]
print(solution(lotteries))