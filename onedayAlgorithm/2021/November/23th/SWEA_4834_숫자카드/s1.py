import sys
sys.stdin = open("input.txt", "r")

def number_cards(N : int, A : str):

    # 주어지는 카드는 0 ~ 9장으로 총 10장이다.
    cards = [0] * 10
    # 먼저 문자열을 돌면서 count array에 숫자를 저장한다.
    for s in A:
        cards[int(s)] += 1

    max_num = 0
    max_card = 0
    # 카드의 장수가 같을 경우에는 숫자가 큰 것을 반환하기 때문에 뒤에서부터 본다.
    for i in range(9, 0, -1):
        if cards[i] > max_num:
            max_num = cards[i]
            max_card = i

    # return값은 가장 많은 카드의 숫자와 장 수를 리턴한다.
    return max_card, max_num

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = input()
    result = number_cards(N, A)
    print("#{} {} {}".format(tc, result[0], result[1]))
