import sys
from collections import deque
sys.stdin = open("5_10.txt", "r")
N, M = map(int, input().split())
ice_block = [list(map(int, input())) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

cnt = 1
for i in range(N):
    for j in range(M):
        if ice_block[i][j] == 0:
            cnt += 1
            queue = deque()
            queue.append([i, j])
            ice_block[i][j] = cnt
            while queue:
                v = queue.popleft()
                for k in range(4):
                    n_r = v[0] + dr[k]
                    n_c = v[1] + dc[k]
                    if 0 <= n_r < N and 0 <= n_c < M and ice_block[n_r][n_c] == 0:
                        ice_block[n_r][n_c] = cnt
                        queue.append([n_r, n_c])

print(cnt - 1)
print(ice_block)