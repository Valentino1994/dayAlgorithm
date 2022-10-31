import sys
sys.stdin = open("input.txt")

N = int(input())
HP = list(map(int, input().split(" ")))
JOY = list(map(int, input().split(" ")))


DP = [[0 for _ in range(100)] for _ in range(N+1)]

for i in range(N+1):
    # 100은 포함하지 않음
    for j in range(100):
        if i == 0 or j == 0:
            DP[i][j] = 0
        elif HP[i-1] <= j:
            DP[i][j] = max(JOY[i-1] + DP[i-1][j-HP[i-1]], DP[i-1][j])
        else:
            DP[i][j] = DP[i-1][j]

# 100은 포함 X
print(DP[N][99])