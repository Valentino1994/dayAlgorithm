import sys
sys.stdin = open("input.txt")

def findStart(building):
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if building[i][j][k] == 'S':
                    return (i, j, k)

answer = 987654321

# 시계방향, 위, 아래
dl = [0, 0, 0, 0, -1, 1]
dr = [-1, 0, 1, 0, 0, 0]
dc = [0, 1, 0, -1, 0, 0]

def dfs(building, cnt, visited, now_position, L, R, C):
    global answer

    if cnt >= answer:
        return

    l, r, c = now_position
    for i in range(len(dl)):
        nl = l + dl[i]
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nl < L and 0 <= nr < R and 0 <= nc < C:
            if building[nl][nr][nc] == 'E':
                answer = min(cnt + 1, answer)
            elif building[nl][nr][nc] == '.' and visited[nl][nr][nc] == 0:
                visited[nl][nr][nc] = 1
                dfs(building, cnt + 1, visited, (nl, nr, nc), L, R, C)
                visited[nl][nr][nc] = 0

    return

while True:

    L, R, C = list(map(int, input().split(" ")))
    if L == 0 and R == 0 and C == 0:
        break

    building = []
    visited = [[[0 for _ in range(C)] for _ in range(R)] for _ in range(L)]

    for i in range(L):
        temp = []
        for _ in range(R):
            temp.append(list(input()))
        building.append(temp)
        input()

    answer = 987654321
    dfs(building, 0, visited, findStart(building), L, R, C)

    if answer == 987654321:
        print("Trapped!")
    else:
        print(f"Escaped in {answer} minute(s).")


