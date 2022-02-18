import sys
sys.stdin = open("input.txt")
from pprint import pprint

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

result = 0
aircon = []
for i in range(N):
    for j in range(M):
        if lab[i][j] == 9:
            aircon.append([i, j])
            visited[i][j] = 1

if not aircon:
    print(0)
# 0: 동 | 1: 남 | 2: 서 | 3: 북
direction = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}

while aircon:
    now = aircon.pop()
    r, c = now[0], now[1]
    result += 1
    visited[r][c] = 1
    # 먼저 aircon에서 뒤의 하나의 위치를 꺼내서 4방향을 넣어준다.
    stack = []
    for i in range(4):
        d_r, d_c = r + direction[i][0], c + direction[i][1]
        if 0 <= d_r < N and 0 <= d_c < M:
            # 방향 체크를 위해 방향도 넣어준다.
            stack.append([d_r, d_c, i])

    # 그 다음 한 방향마다 갈 수 있는 위치를 다 한다.
    while stack:
        # 현재 위치를 꺼낸다.
        next_place = stack.pop()
        # 꺼낼 수 있다는 건 무조건 갈 수 있다는 거니까 result 더해주고, 9로 바꿔준다.
        now_r, now_c, now_d = next_place[0], next_place[1], next_place[2]
        visited[now_r][now_c] = 1
        next_r, next_c = now_r + direction[now_d][0], now_c + direction[now_d][1]
        # 만약 벽이라면 다음으로 넘어간다.
        if not (0 <= now_r < N and 0 <= now_c < M):
            continue

        # 만약 1번 물건이라면
        if lab[now_r][now_c] == 1:
            # 만약 1번 물건인데 현재 방향이 0 혹은 2라면 (동서라면) 다음은 넣을 수 없다.
            if now_d == 0 or now_d == 2:
                continue
            # 그게 아니라면 현재 방향대로 간다.
            else:
                if 0 <= next_r < N and 0 <= next_c < M:
                    stack.append([next_r, next_c, now_d])
        # 만약 2번 물건이라면 1번과 방향만 다를 뿐 그대로 간다.
        elif lab[now_r][now_c] == 2:
            if now_d == 1 or now_d == 3:
                continue
            else:
                if 0 <= next_r < N and 0 <= next_c < M:
                    stack.append([next_r, next_c, now_d])
        # 만약 3번 물건이라면
        elif lab[now_r][now_c] == 3:
            if now_d == 0:
                if 0 <= now_c + direction[3][0] < N and 0 <= now_c + direction[3][1] < M:
                    stack.append([now_r + direction[3][0], now_c + direction[3][1], 3])
            elif now_d == 1:
                if 0 <= now_r + direction[2][0] < N and 0 <= now_c + direction[2][1] < M:
                    stack.append([now_r + direction[2][0], now_c + direction[2][1], 2])
            elif now_d == 2:
                if 0 <= now_r + direction[1][0] < N and 0 <= now_r + direction[1][1] < M:
                    stack.append([now_r + direction[1][0], now_c + direction[1][1], 1])
            elif now_d == 3:
                if 0 <= now_r + direction[0][0] < N and 0 <= now_r + direction[0][1] < M:
                    stack.append([now_r + direction[0][0], now_c + direction[0][1], 0])
        # 만약 4번 물건이라면
        elif lab[now_r][now_c] == 4:
            if now_d == 0:
                if 0 <= now_r + direction[1][0] < N and 0 <= now_r + direction[1][1] < M:
                    stack.append([now_r + direction[1][0], now_c + direction[1][1], 1])
            elif now_d == 1:
                if 0 <= now_r + direction[0][0] < N and 0 <= now_r + direction[0][1] < M:
                    stack.append([now_r + direction[0][0], now_c + direction[0][1], 0])
            elif now_d == 2:
                if 0 <= now_r + direction[3][0] < N and 0 <= now_r + direction[3][1] < M:
                    stack.append([now_r + direction[3][0], now_c + direction[3][1], 3])
            elif now_d == 3:
                if 0 <= now_r + direction[2][0] < N and 0 <= now_c + direction[2][1] < M:
                    stack.append([now_r + direction[2][0], now_c + direction[2][1], 2])
        # 이미 에어컨이 지나갔더라도 바람이 또 지나갈 수 도 있으니까 0일 때로 하면 안되고 else로 처리한다.
        else:
            if 0 <= next_r < N and 0 <= next_c < M:
                stack.append([next_r, next_c, now_d])

answer = 0
for i in range(N):
    answer += sum(visited[i])

print(answer)
pprint(visited)


