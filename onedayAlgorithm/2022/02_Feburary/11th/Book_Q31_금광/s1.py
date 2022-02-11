import sys
sys.stdin = open("input.txt", "r")

T = int(input())
N, M = map(int, input().split())
info = list(map(int, input().split()))
mine = []

for i in range(0, len(info), M):
    mine.append(info[i:i+M])

# 좌상, 좌, 좌하를 확인
dr = [-1, 0, 1]
dc = [-1, -1, -1]
for i in range(1, M):
    tmp = []
    for j in range(N):
        for k in range(3):
            n_r, n_c = j + dr[k], i + dc[k]
            if 0 <= n_r < N and 0 <= n_c < M:
                tmp.append(mine[n_r][n_c])
        mine[j][i] += max(tmp)

result = 0
for i in range(N):
    if mine[i][-1] > result:
        result = mine[i][-1]

print(result)