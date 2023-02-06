import sys
sys.stdin = open("input.txt")


t = int(input())
for tc in range(t):
    m, n, k = list(map(int, input().split(" ")))
    board = [[0 for _ in range(m)] for _ in range(n)]

    for _ in range(k):
        x, y = list(map(int, input().split(" ")))
        board[y][x] = 1

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    result = 0
    for i in range(n):
        for j in range(m):

            if board[i][j] == 1:
                result += 1
                board[i][j] = 0
                queue = [[i, j]]
                queue_index = 0

                while len(queue) > queue_index:
                    r, c = queue[queue_index]
                    for l in range(len(dr)):
                        nr = r + dr[l]
                        nc = c + dc[l]
                        if 0 <= nr < n and 0 <= nc < m and board[nr][nc] == 1:
                            board[nr][nc] = 0
                            queue.append([nr, nc])

                    queue_index += 1

    print(result)

