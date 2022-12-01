import sys
sys.stdin = open("input.txt")

def answer():
    N = int(input())
    board = []
    for _ in range(2):
        board.append(list(map(int, input().split(" "))))


    # 버린다는 선택지는 어떻게 하게 할 수 있을까.
    DP_UP = [0] * N
    DP_DOWN = [0] * N

    for i in range(N):
        if i % 2 == 0:
            DP_UP[i] = board[0][i]
            DP_DOWN[i] = board[1][i]
        else:
            DP_UP[i] = board[1][i]
            DP_DOWN[i] = board[0][i]

    print(sum(DP_UP))
    print(sum(DP_DOWN))

    return

T = int(input())
for _ in range(T):
    answer()

