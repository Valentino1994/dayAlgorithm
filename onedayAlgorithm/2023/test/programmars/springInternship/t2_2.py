def solution(grid):
    answer = 0

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    big_r = len(grid)
    big_c = len(grid[0])
    visited = [[0 for _ in range(big_c)] for _ in range(big_r)]

    for i in range(big_r):
        for j in range(big_c):
            if grid[i][j] == "#":
                answer += 1
                visited[i][j] = 1
                continue

            elif visited[i][j] == 0:
                validate = True
                queue = [[i, j]]
                queue_index = 0

                while queue_index < len(queue):
                    r, c = queue[queue_index]
                    visited[r][c] = 1

                    for k in range(len(dr)):
                        nr = r + dr[k]
                        nc = c + dc[k]

                        # 벽에 도달하였다면 validate를 False로 줌
                        if nr < 0 or nr >= big_r or nc < 0 or nc >= big_c:
                            validate = False
                            continue

                        # 벽이 아닌데 . 이면 q에 추가
                        if grid[nr][nc] == "." and visited[nr][nc] == 0:
                            if [nr, nc] not in queue:
                                queue.append([nr, nc])

                    queue_index += 1

                if validate:
                    answer += len(queue)

    return answer

grid = [".....####", "..#...###", ".#.##..##", "..#..#...", "..#...#..", "...###..."]
print(solution(grid))