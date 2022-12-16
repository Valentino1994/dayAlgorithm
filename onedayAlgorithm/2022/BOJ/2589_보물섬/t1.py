import sys
sys.stdin = open("input.txt")

R, C = list(map(int, input().split(" ")))
island_map = []
for _ in range(R):
    island_map.append(list(map(int, input().replace('W', '0').replace("L", '1'))))

visited = [[0 for _ in range(C)] for _ in range(R)]

queue = []
for i in range(R):
    for j in range(C):
        if island_map[i][j] == 1:
            queue.append((i, j))
            break

# 상 우 하 좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
queue_index = 0
while queue_index < len(queue):
    r, c = queue[queue_index]
    now_sec = island_map[r][c]
    for i in range(len(dr)):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < R and 0 <= nc < C and island_map[nr][nc] != 0 and visited[nr][nc] == 0:
            island_map[nr][nc] = now_sec + 1
            visited[nr][nc] = 1
            queue.append((nr, nc))

    queue_index += 1

print(island_map)
