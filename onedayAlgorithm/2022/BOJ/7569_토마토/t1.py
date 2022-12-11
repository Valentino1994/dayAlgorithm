import sys
sys.stdin = open("input.txt")

M, N, H = list(map(int, input().split(" ")))

# 3 dimensions BFS
tomato_boards = []

for _ in range(H):
    board_for_row = []
    for _ in range(N):
        board_for_row.append(list(map(int, input().split(" "))))
    tomato_boards.append(board_for_row)

def find_start_points():
    tomatos_from_start = []

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomato_boards[i][j][k] == 1:
                    tomatos_from_start.append([i, j, k])

    return tomatos_from_start

def check_wall(nz, ny, nx):

    if not (0 <= nz < H):
        return False
    if not (0 <= ny < N):
        return False
    if not (0 <= nx < M):
        return False

    if tomato_boards[nz][ny][nx] != 0:
        return False

    return True

def find_answer():
    result = 0

    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomato_boards[i][j][k] == 0:
                    return -1
                else:
                    result = max(result, tomato_boards[i][j][k])

    return result - 1

def bfs():
    # Upper Z, Lower Z, Upper Y, Upper X, Lower Y, Lower X
    dz = [-1, 1, 0, 0, 0, 0]
    dy = [0, 0, -1, 0, 1, 0]
    dx = [0, 0, 0, 1, 0, -1]

    tomato_queue = find_start_points()
    queue_index = 0
    while queue_index < len(tomato_queue):

        z, y, x = tomato_queue[queue_index]
        for i in range(6):
            nz = z + dz[i]
            ny = y + dy[i]
            nx = x + dx[i]
            wall_pointer = check_wall(nz, ny, nx)
            if wall_pointer:
                tomato_queue.append([nz, ny, nx])
                tomato_boards[nz][ny][nx] = tomato_boards[z][y][x] + 1

        queue_index += 1

    answer = find_answer()

    return answer

print(bfs())


