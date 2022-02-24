import sys
sys.stdin = open("input.txt", "r")
from pprint import pprint
R, C = map(int, input().split())

board = []
jonsu_positon = []
crazy_position = []
for i in range(R):
    now = input()
    tmp = []
    for j in range(C):
        if now[j] == "I":
            tmp.append(1)
            jonsu_positon = [i, j]
        elif now[j] == "R":
            crazy_position.append([i, j])
            tmp.append(2)
        else:
            tmp.append(0)
    board.append(tmp)

# 1은 남서, 2는 정남, 3은 남동, 4는 정서, 5는 안움직임, 6은 정동, 7은 북서, 8은 정북, 9는 북동
move_direction = [(0, 0), (1, -1), (1, 0), (1, 1), (0, -1), (0, 0), (0, 1), (-1, -1), (-1, 0), (-1, 1)]

def jonsu_move(r: int, c: int, direction: int):
    # 종수는 그저 움직이며 움직였을 때 아두이노랑 안겹치면 True 겹치면 False를 뱉는다.
    d = direction
    n_r, n_c = r + move_direction[d][0], c + move_direction[d][1]

    # board를 벗어나는 명령은 주어지지 않으니까 비어있는 칸일 경우에는 이동시키고 아니면 False.
    if board[n_r][n_c] == 0 or board[n_r][n_c] == 1:
        board[r][c] = 0
        board[n_r][n_c] = 1
        return [n_r, n_c]

    return 0

def crazy_move(r: int, c: int, j_r: int, j_c: int):

    # 가장 멀리 떨어질 수 있는 것은 보드의 크기 정도
    min_value = R * C
    re_r = 0
    re_c = 0
    for i in range(1, 10):
        n_r = r + move_direction[i][0]
        n_c = c + move_direction[i][1]
        distance = abs(n_r - j_r) + abs(n_c - j_c)
        if 0 <= n_r < R and 0 <= n_c < C and distance < min_value:
            min_value = distance
            re_r = n_r
            re_c = n_c

    if board[re_r][re_c] == 0:
        board[r][c] = 0
        board[re_r][re_c] = 2
        return [re_r, re_c]

    elif board[re_r][re_c] == 1:
        return 0

    elif board[re_r][re_c] == 2:
        board[r][c] = 0
        board[re_r][re_c] += 2
        return [re_r, re_c]

command = input()
result = 0
flag = True
for i in range(len(command)):
    c = int(command[i])
    result += 1
    now = jonsu_move(jonsu_positon[0], jonsu_positon[1], c)
    if not now:
        print("kraj {}".format(result))
        flag = False
        break
    jonsu_positon[0] = now[0]
    jonsu_positon[1] = now[1]

    for crazy in crazy_position:
        now = crazy_move(crazy[0], crazy[1], jonsu_positon[0], jonsu_positon[1])
        if not now:
            print("kraj {}".format(result))
            flag = False
            break
        crazy[0] = now[0]
        crazy[1] = now[1]

    for crazy in crazy_position:
        if board[crazy[0]][crazy[1]] > 2:
            board[crazy[0]][crazy[1]] = 0

print(jonsu_positon)
print(crazy_position)
print(board)
