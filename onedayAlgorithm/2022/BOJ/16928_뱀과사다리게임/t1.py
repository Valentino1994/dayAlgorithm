import sys
sys.stdin = open("input.txt")

N, M = list(map(int, input().split(" ")))
ladder_start = []
ladder_end = []
snake_start = []
snake_end = []

for _ in range(N):
    s, e = list(map(int, input().split(" ")))
    ladder_start.append(s)
    ladder_end.append(e)

for _ in range(M):
    s, e = list(map(int, input().split(" ")))
    snake_start.append(s)
    snake_end.append(e)

board = [987654321 for _ in range(101)]
answer = 987654321

def dfs(cnt, position):
    global answer

    if position >= 100:
        answer = min(answer, cnt)
        return

    for i in range(6, 0, -1):
        next_position = position + i
        if next_position in snake_start:
            continue

        for j in range(N):
            if next_position == ladder_start[j]:
                next_position = ladder_end[j]

        for k in range(M):
            if next_position == snake_end[k]:
                next_position = snake_start[k]

        if next_position <= 100 and board[next_position] > cnt + 1:
            for l in range(position, next_position + 1):
                board[l] = cnt + 1
            dfs(cnt + 1, next_position)

    return

dfs(0, 1)
print(answer)