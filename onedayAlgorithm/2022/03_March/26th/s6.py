def buy(member, req, buy_pending, sell_pending, accounts):
    # 구매 요청의 경우 buy_pending에서 가능한 판매요청을 찾는다.
    req_amount, req_price = req[1], req[2]

    # 먼저 sell_pending이 비어있을 경우 바로 buy_pending에 넣고 종료한다.
    if not buy_pending:
        buy_pending.append([member, req_amount, req_price])
        return req, buy_pending, sell_pending, accounts

    return req, buy_pending, sell_pending, accounts


def sell(member, req, buy_pending, sell_pending, accounts):
    req_amount, req_price = req[1], req[2]

    # 먼저 buy_pending이 비어있을 경우 바로 sell_pending에 넣고 종료한다.
    if not buy_pending:
        sell_pending.append([member, req_amount, req_price])
        return req, buy_pending, sell_pending, accounts

    # 판매 요청의 경우 buy_pending에서 가능한 구매요청을 찾는다.
    # 찾는 방법은
    # 1. sell_price 이상일 것
    # req = Type, Amount, Price임으로
    buy_arr = []
    for info in buy_pending:
        print(info)

    return req, buy_pending, sell_pending, accounts


def solution(req_id, req_info):
    answer = []

    # 계좌의 정보를 담아둔다.
    accounts = dict()

    buy_pending = []
    sell_pending = []

    for i in range(len(req_info)):
        req = req_info[i]
        member = req_id[i]

        # 구매할 경우
        if req[0] == 0:
            new_state = buy(member, req, buy_pending, sell_pending, accounts)
            buy_pending = new_state[1]
            sell_pending = new_state[2]
            accounts = new_state[3]

        # 판매할 경우
        else:
            new_state = sell(member, req, buy_pending, sell_pending, accounts)
            buy_pending = new_state[1]
            sell_pending = new_state[2]
            accounts = new_state[3]

    return answer