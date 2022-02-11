import sys
from pprint import pprint
sys.stdin = open("input.txt", "r")

N = int(input())
triangle = [[0] * (2 * N - 1) for _ in range(N)]
triangle[0][N - 1] = int(input())
idx = N - 2
for i in range(1, N):
    info = list(map(int, input().split()))
    info_idx = 0
    for j in range(idx, 2*N, 2):
        if info_idx >= len(info):
            break
        triangle[i][j] = info[info_idx]
        info_idx += 1
    idx -= 1

idx = N - 2
for i in range(1, N):
    for j in range(idx, 2*N-1, 2):
        tmp = []
        if j-1 >= 0:
            tmp.append(triangle[i-1][j-1])
        if j+1 < 2*N-1:
            tmp.append(triangle[i-1][j+1])
        triangle[i][j] += max(tmp)
    idx -= 1
print(max(triangle[N-1]))
pprint(triangle)