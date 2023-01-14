import sys
sys.stdin = open("input2.txt")

N, M = list(map(int, input().split(" ")))
earth = []
for _ in range(N):
    earth.append(list(map(int, input().split(" "))))

visited = [[0 for _ in range(M)] for _ in range(N)]

def check_next(r, c):
    nr = r
    nc = c

    if r < 0:
        nr = N - 1
    elif r >= N:
        nr = 0

    if c < 0:
        nc = M - 1
    elif c >= M:
        nc = 0

    return (nr, nc)

# 시계순
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(i, j):
    queue = [(i, j)]
    queue_index = 0

    while queue_index < len(queue):
        r, c = queue[queue_index]

        for k in range(4):
            nr, nc = check_next(r + dr[k], c + dc[k])
            if earth[nr][nc] == 0 and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                queue.append((nr, nc))

        queue_index += 1

answer = 0
for i in range(N):
    for j in range(M):
        if earth[i][j] == 0 and visited[i][j] == 0:
            answer += 1
            bfs(i, j)

print(answer)