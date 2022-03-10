import sys
from pprint import pprint
sys.stdin = open("input.txt", "r")

R, C = map(int, input().split())
mine = [list(input()) for _ in range(R)]

c = int(input())
commands = list(map(int, input().split()))

# up, down, left, right
direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def air_check(i, j):
    global mineral
    stack = [[i, j]]
    while stack:
        r, c = stack.pop()
        if [r, c] not in mineral:
            mineral.append([r, c])
        visited[r][c] = 1
        for i in range(4):
            n_r = r + direction[i][0]
            n_c = c + direction[i][1]
            # if the mineral is on a lands
            if n_r == 0 and 0 <= n_c < C and mine[n_r][n_c] == 'x':
                return False
            elif n_r >= R:
                return False
            # else if the mineral is out of the mine
            elif 0 <= n_r < R and 0 <= n_c < C:
                if mine[n_r][n_c] == 'x' and visited[n_r][n_c] == 0:
                    stack.append([n_r, n_c])
    return True

def falling_down(mineral):
    mineral.sort(key=lambda x: x[1], reverse=True)
    columns = []
    min_height = 987654321
    # calculate minimum height
    for i in range(len(mineral)-1, -1, -1):
        if mineral[i][1] not in columns:
            cnt = 0
            r, c = mineral[i]
            columns.append(c)
            while True:
                r += 1
                if 0 <= r < R and mine[r][c] == '.':
                    cnt += 1
                    continue
                else:
                    if cnt < min_height:
                        min_height = cnt
                    break

    for m in mineral:
        r, c = m
        mine[r][c] = '.'
    for m in mineral:
        r = m[0] + min_height
        c = m[1]
        mine[r][c] = 'x'

    return

for index, command in enumerate(commands):
    # R is a land so I should calculate real position
    r = R - command
    # if the command is on odd number turn, starts from left, or not starts from right
    if index % 2 == 0:
        c = 0
    else:
        c = C-1
    while True:
        flag = True
        # if the stick meets a wall, end
        if not 0 <= c < C:
            break
        # if the stick meets a mineral, erase it and check the mine
        if mine[r][c] == 'x':
            mine[r][c] = '.'
            visited = [[0] * C for _ in range(R)]
            for i in range(R):
                for j in range(C):
                    mineral = []
                    if mine[i][j] == 'x' and visited[i][j] == 0:
                        if not air_check(i, j):
                            flag = False
                            break
                        else:
                            flag = False
                            falling_down(mineral)
                            break
        if not flag:
            break

        if index % 2 == 0:
            c += 1
        else:
            c -= 1

for m in mine:
    print(*m)