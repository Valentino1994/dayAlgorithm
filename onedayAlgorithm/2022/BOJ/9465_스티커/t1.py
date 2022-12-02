import sys
sys.stdin = open("input.txt")

def solution():
    N = int(input())
    board = []
    for _ in range(2):
        board.append(list(map(int, input().split(" "))))

    DP = [[0] * (N+1) for _ in range(2)]
    DP[0][1] = board[0][0]
    DP[1][1] = board[1][0]

    for i in range(2, N+1):
        DP[0][i] = max(DP[1][i-1], DP[1][i-2]) + board[0][i-1]
        DP[1][i] = max(DP[0][i-1], DP[0][i-2]) + board[1][i-1]

    return max(max(DP[0]), max(DP[1]))

T = int(input())
for _ in range(T):
    answer = solution()
    print(answer)

