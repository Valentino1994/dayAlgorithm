import sys
sys.stdin = open("input.txt", 'r')
#input = sys.stdin.readline

N, M = map(int, input().split())
IN = [[0] * M for _ in range(N)]

for i in range(N):
    populations = list(map(int, input().split()))
    IN[i][0] = populations[0]
    for j in range(1, M):
        IN[i][j] = populations[j] + IN[i][j-1]

C = int(input())
areas = []
for _ in range(C):
    areas.append(list(map(int, input().split())))

for area in areas:
    answer = 0
    r1, c1, r2, c2 = area[0] - 1, area[1] - 1, area[2] - 1, area[3] - 1
    if c1 == 0:
        for i in range(r1, r2 + 1):
            answer += IN[i][c2]
    else:
        for i in range(r1, r2 + 1):
            answer += (IN[i][c2] - IN[i][c1 - 1])
    print(answer)
