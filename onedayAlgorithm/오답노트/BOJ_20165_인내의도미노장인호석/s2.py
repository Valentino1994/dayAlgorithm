from sys import stdin

readline = stdin.readline

N, M, R = map(int, readline().split())
board = [list(map(int, readline().split())) for _ in range(N)]
is_down = [[False for _ in range(M)] for _ in range(N)]
dir_map = {"E": 0, "W": 1, "S": 2, "N": 3}
D = ((0, 1), (0, -1), (1, 0), (-1, 0))


def solve():
    count = 0
    for _ in range(R):
        line = readline().split()
        row, col, _dir = int(line[0]) - 1, int(line[1]) - 1, dir_map[line[2]]

        if not is_down[row][col]:
            count += dfs(row, col, _dir, board[row][col]) + 1

        line = readline().split()
        row, col = int(line[0]) - 1, int(line[1]) - 1

        is_down[row][col] = False

    print(count)
    for i in range(N):
        for j in range(M):
            if is_down[i][j]:
                print("F", end=" ")
            else:
                print("S", end=" ")
        print()


def dfs(row, col, _dir, length):
    is_down[row][col] = True
    total = 0

    if length > 1:
        nr, nc = row + D[_dir][0], col + D[_dir][1]

        if 0 <= nr < N and 0 <= nc < M:
            if not is_down[nr][nc]:
                total += 1
                length = max(length - 1, board[nr][nc])
            else:
                length -= 1

            total += dfs(nr, nc, _dir, length)

    return total

solve()