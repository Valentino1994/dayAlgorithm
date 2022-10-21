import sys
sys.stdin = open("input.txt", "r")

n, m = list(map(int, input().split(" ")))
board = []
for _ in range(n):
    board.append(list(map(int, input().split(" "))))

answer = 0
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def bfs(board):

    for i in (n):
        for j in range(m):
            if board == 2:
                queue = [[i, j]]
                queue_index = 0
                while queue_index < len(queue):
                    now = queue[queue_index]
                    for i in range(4):
                        nr = now[0] + dr[i]
                        nc = now[1] + dc[i]
                        if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == 0:
                            board[nr][nc] = 2
                            queue.append([nr, nc])

    return 0

def dfs(cnt):
    global answer

    if cnt == 3:
        temp = bfs(board[:])
        answer = max(temp, answer)

    return

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            dfs()


