import sys
from collections import deque
from pprint import pprint
sys.stdin = open("input.txt", "r")

N, M, R = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

round = []
for i in range(0, 2*R, 2):
    tmp = []
    for _ in range(2):
        tmp.append(input())
    round.append(tmp)

visited = [[0] * M for _ in range(N)]

direction = {"E": (0, 1), "W": (0, -1), "S": (1, 0), "N": (-1, 0)}
result = 0

for i in range(R):
    attack = round[i][0]
    defence = round[i][1]
    a_r, a_c, a_d = attack.split(' ')
    d_r, d_c = defence.split(' ')
    # 공격
    # 인덱스로 접근하기 위해 시작에서는 -1씩 해준다.
    q = deque([[int(a_r) - 1, int(a_c) - 1]])
    while q:
        v = q.popleft()
        # -1 씩 해준 상태이기 때문에 바로 뽑는다.
        n_r, n_c = v[0], v[1]
        # 이미 넘어진 칸을 건드리려고 하면 아무일도 일어나지 않는다.
        if visited[n_r][n_c] == 1:
            break
        # 칸에 적힌 숫자만큼 반복한다. 2이면 본인의 칸 + 1 칸 이지만
        # 이미 heap에서 꺼내면서 방문체크를 하기 때문에 range를 nums-1까지만 보면 된다.
        visited[n_r][n_c] = 1
        result += 1
        nums = board[n_r][n_c]
        for _ in range(nums - 1):
            n_r = n_r + direction[a_d][0]
            n_c = n_c + direction[a_d][1]
            # 해당하는 방향으로 이동했을 때 board를 넘어가면 break
            if n_c < 0 or n_c >= M or n_r < 0 or n_r >= N:
                break
            # 만약 방문하지 않은 곳이면 q에 추가해준다.
            if visited[n_r][n_c] == 0:
                q.append([n_r, n_c])
    # 방어
    # 방어하려고 한 곳이 쓰러지지 않은 곳이라면 아무일도 일어나지 않는다.
    if visited[int(d_r) - 1][int(d_c) - 1] == 0:
        continue
    else:
        visited[int(d_r) - 1][int(d_c) - 1] = 0

n_board = []
for i in range(N):
    tmp = ''
    for j in range(M):
        if visited[i][j] == 1:
            tmp += 'F '
        else:
            tmp += 'S '
    n_board.append(tmp[:len(tmp)])

print(result)
for _ in range(N):
    print(n_board[_])
