from pprint import pprint

def solution(rows, columns, lands):
    answer = []

    matrix = [ [0] * columns for _ in range(rows)]

    for land in lands:
        r, c = land
        matrix[r-1][c-1] = 1

    # 땅이 아닌 곳이 바다인지 호수인지 아닌지 먼저 체크함
    # 시계 방향
    # 모든 map을 돌면서 현재 물이라면 시작
    for i in range(rows):
        for j in range(columns):
            n_r, n_c = i, j
            if matrix[n_r][n_c] == 0:
                if checkLake(n_r, n_c, rows, columns, matrix):
                    continue

                matrix = makeSea(n_r, n_c, rows, columns, matrix)

    answer = countLake(rows, columns, matrix)

    return answer

def checkLake(r, c, rows, columns, matrix):

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    for i in range(4):
        flag = True
        n_r = r
        n_c = c

        while matrix[n_r][n_c] != 1:

            n_r += dr[i]
            n_c += dc[i]

            if not (0 <= n_r < rows and 0 <= n_c < columns):
                flag = False
                break

            elif matrix[n_r][n_c] == -1:
                flag = False
                break

        if not flag:
            return False

    return True

def makeSea(r, c, rows, columns, matrix):

    now_map = matrix

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    que = [[r, c]]
    while que:

        now = que.pop(0)
        now_map[now[0]][now[1]] = -1

        for i in range(4):

            n_r = now[0] + dr[i]
            n_c = now[1] + dc[i]

            if 0 <= n_r < rows and 0 <= n_c < columns:
                if now_map[n_r][n_c] == 0:
                    que.append([n_r, n_c])

    return now_map

def countLake(rows, columns, matrix):

    lakes = []
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    for i in range(rows):
        for j in range(columns):
            count = 0

            if matrix[i][j] == 0:
                que = [[i, j]]
                while que:

                    now = que.pop(0)
                    matrix[now[0]][now[1]] = 2
                    count += 1

                    for k in range(4):

                        n_r = now[0] + dr[k]
                        n_c = now[1] + dc[k]

                        if 0 <= n_r < rows and 0 <= n_c < columns:
                            if matrix[n_r][n_c] == 0:
                                que.append([n_r, n_c])

                lakes.append(count)
    if lakes:
        return [min(lakes), max(lakes)]
    else:
        return [-1, -1]

rows = 5
columns = 6
lands = [[2, 2], [2, 3], [2, 4], [3, 2], [3, 5], [4, 3], [4, 4]]

print(solution(rows, columns, lands))