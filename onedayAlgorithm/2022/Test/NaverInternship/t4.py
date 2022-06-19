def solution(B):
    result = [0, 0, 0]
    # up, right, down, left
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    R = len(B)
    C = len(B[0])

    visited = [[0] * C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if B[i][j] == "#" and visited[i][j] == 0:
                count = 0
                que = [[i, j]]

                while que:
                    now = que.pop(0)
                    r, c = now[0], now[1]
                    visited[r][c] = 1
                    count += 1
                    for k in range(4):
                        nr = r + dr[k]
                        nc = c + dc[k]
                        if 0 <= nr < R and 0 <= nc < C and B[nr][nc] == "#" and visited[nr][nc] == 0:
                            que.append([nr, nc])

                if count >= 3:
                    result[2] += 1
                elif count == 2:
                    result[1] += 1
                elif count == 1:
                    result[0] += 1

    return result

B = ["##.", "#.#", ".##"]

print(solution(B))