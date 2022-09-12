def solution(R):
    result = 1

    # up, right, down, left
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    # robot is looking at right at first
    now_direction = 1
    # and it is on 0, 0 at first
    now_position = [0, 0]

    r = len(R)
    c = len(R[0])

    visited = [[0] * c for _ in range(r)]
    visited[0][0] = 1
    count = 0
    while True:
        nr = now_position[0] + dr[now_direction]
        nc = now_position[1] + dc[now_direction]

        # if there is not a wall or not a box on nextStep
        if 0 <= nr < r and 0 <= nc < c and R[nr][nc] != "X":
            if visited[nr][nc] > 2:
                break
            elif visited[nr][nc] == 0:
                visited[nr][nc] += 1
                now_position = [nr, nc]
                result += 1
                count = 0
            else:
                visited[nr][nc] += 1
                now_position = [nr, nc]
                count = 0

        else:
            count += 1
            if count == 3:
                break
            now_direction = (now_direction + 1) % 4

    return result

R = ["...X..", "....XX", "..X..."]
R1 = ["....X..", "X......", ".....X.", "......."]
R2 = ["...X.", ".X..X", "X...X", "..X.."]

print(solution(R))
print(solution(R1))
print(solution(R2))