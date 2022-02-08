import sys
sys.stdin = open("input.txt", "r")
#input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())
IN = [list(map(int, input().split())) for _ in range(N)]

movement = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)}
rotate_cnt = 0
while True:
    IN[r][c] = -1
    # 왼쪽 방향으로 회전한다.
    if d == 3:
        d = 0
    else:
        d += 1

    n_r = r + movement[d][0]
    n_c = c + movement[d][1]
    # 왼쪽 방향에 0이면 한 칸 전진
    if IN[n_r][n_c] == 0:
        r = n_r
        c = n_c
    # 그렇지 않다면 회전만 하고 continue
    elif rotate_cnt < 4:
        rotate_cnt += 1
        continue
    # 네 방향 모두 이동할 수 없다면 (이미 가본 칸, 바다인 칸)
    # 방향 유지 후 뒤로 한 칸 이동
    n_r = r - movement[d][0]
    n_c = c - movement[d][1]
    if IN[n_r][n_c] == 1:
        break
    # 이 때 뒤 칸이 바다이면 break

result = 0
for i in range(N):
    for j in range(M):
        if IN[i][j] == -1:
            result += 1

print(result)