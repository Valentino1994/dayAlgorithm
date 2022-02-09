import sys
from collections import deque
sys.stdin = open("5_11.txt", "r")

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]

N, M = N-1, M-1
queue = deque()
queue.append([0, 0])
maze[0][0] = 2

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

while queue:
    v = queue.popleft()
    r, c = v[0], v[1]
    for i in range(4):
        n_r = r + dr[i]
        n_c = c + dc[i]
        if 0 <= n_r <= N and 0 <= n_c <= M and maze[n_r][n_c] == 1:
            queue.append([n_r, n_c])
            maze[n_r][n_c] = maze[r][c] + 1

print(maze[N][M] - 1)