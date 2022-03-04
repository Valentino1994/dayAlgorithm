import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())
board = [input() for _ in range(N)]

flag = False
cnt = 0
# 좌 우 상 하
movement = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def move(direction: int, red: list, blue: list, board: list):
    n_red = red
    n_blue = blue
    p_red = True
    p_blue = True
    while True:
        r_r = n_red[0] + movement[direction][0]
        r_c = n_red[1] + movement[direction][1]
        b_r = n_blue[0] + movement[direction][0]
        b_c = n_blue[1] + movement[direction][1]
        # 만약 벽이거나 상대 구슬이 있으면 움직일 수 없다.
        if board[r_r][r_c] == '#' or board[r_r][r_c] == 'B':
            r_r -= movement[direction][0]
            r_c -= movement[direction][1]
            p_red = False
        if board[b_r][b_c] == '#' or board[b_r][b_c] == 'R':
            b_r -= movement[direction][0]
            b_c -= movement[direction][1]
            p_blue = False

        # 파란색이 먼저 떨어지거나 동시에 떨어지면 실패
        if board[b_r][b_c] == 'O':
            return

        if board[r_r][r_c] == 'O':
            flag = True
            return

        n_red = [r_r, r_c]
        n_blue = [b_r, b_c]
        
    return

def beads(red: list, blue: list, board: list, cnt: int):

    if flag:
        return

    if cnt == 10:
        return

    # 4방향을 돌리는데, board의 위치를 바꾼다.
    for i in range(4):
        n_board = move(i, red, blue, board[:])
        if n_board:
            beads(red, blue, n_board, cnt + 1)

