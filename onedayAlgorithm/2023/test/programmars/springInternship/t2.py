def calculate_width(row_dictionary):
    result = 0

    for columns in row_dictionary.values():
        result += (max(columns) - min(columns)) + 1

    return result

def solution(grid):
    answer = 0

    dr = [-1, -1, 0, 1, 1, 1, 0, -1]
    dc = [0, 1, 1, 1, 0, -1, -1, -1]

    big_r = len(grid)
    big_c = len(grid[0])
    visited = [[0 for _ in range(big_c)] for _ in range(big_r)]

    for i in range(big_r):
        for j in range(big_c):
            if grid[i][j] == "#" and visited[i][j] == 0:
                row_dictionary = dict()
                queue = [[i, j]]
                queue_index = 0
                while queue_index < len(queue):
                    r, c = queue[queue_index]
                    visited[r][c] = 1

                    if r in row_dictionary:
                        if c not in row_dictionary[r]:
                            row_dictionary[r].append(c)
                    else:
                        row_dictionary[r] = [c]

                    for k in range(len(dr)):
                        nr = r + dr[k]
                        nc = c + dc[k]
                        if 0 <= nr < big_r and 0 <= nc < big_c and grid[nr][nc] == "#" and visited[nr][nc] == 0:
                            queue.append([nr, nc])

                    queue_index += 1
                answer += calculate_width(row_dictionary)
    return answer

grid = [".....####", "..#...###", ".#.##..##", "..#..#...", "..#...#..", "...###..."]

print(solution(grid))