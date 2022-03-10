import sys
sys.stdin = open("input.txt", "r")
from pprint import pprint

N, K = map(int, input().split())
board = dict()
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        board[(i, j)] = [0, []]
        board[(i, j)][0] = tmp[j]

pieces = []
for i in range(K):
    p = list(map(int, input().split()))
    # 0: direction, 1: present place
    pieces.append([p[2], [p[0]-1, p[1]-1]])
    board[(p[0]-1, p[1]-1)][1].append(i)

# 1: right, 2: left, 3: up, 4: down
direction = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}
def turn(index):
    # starts from index
    r, c = pieces[index][1]
    placed_pieces = board[(r, c)][1]
    bottom = placed_pieces[0]

    if placed_pieces:
        for piece in placed_pieces:
            visited[piece] = 1

    d = pieces[bottom][0]
    r, c = pieces[bottom][1]
    n_r = r + direction[d][0]
    n_c = c + direction[d][1]
    # out of board or blue
    if n_c < 0 or n_r < 0 or n_r >= N or n_c >= N or board[(n_r, n_c)][0] == 2:
        if d % 2 == 0:
            d -= 1
        else:
            d += 1
        n_r = r + direction[d][0]
        n_c = c + direction[d][1]
        if n_c < 0 or n_r < 0 or n_r >= N or n_c >= N or board[(n_r, n_c)][0] == 2:
            return
        else:
            for p in board[(r, c)][1]:
                board[(n_r, n_c)][1].append(p)
            board[(r, c)][1] = []
            for p in board[(n_r, n_c)][1]:
                pieces[p][1] = [n_r, n_c]
            if len(board[(n_r, n_c)][1]) >= 4:
                return True

    # or white
    elif board[(n_r, n_c)][0] == 0:
        for p in board[(r, c)][1]:
            board[(n_r, n_c)][1].append(p)
        board[(r, c)][1] = []
        for p in board[(n_r, n_c)][1]:
            pieces[p][1] = [n_r, n_c]
        if len(board[(n_r, n_c)][1]) >= 4:
            return True

    # or red
    elif board[(n_r, n_c)][0] == 1:
        for p in board[(r, c)][1][::-1]:
            board[(n_r, n_c)][1].append(p)
        board[(r, c)][1] = []
        for p in board[(n_r, n_c)][1]:
            pieces[p][1] = [n_r, n_c]
        if len(board[(n_r, n_c)][1]) >= 4:
            return True

    return False

cnt = 0
while cnt < 1000:
    cnt += 1
    visited = [0] * K
    flag = False
    for i in range(K):
        if visited[i] == 0:
            visited[i] = 1
            if turn(i):
                flag = True
                break
    if flag:
        break

if cnt == 1000:
    print(-1)
else:
    print(cnt)
