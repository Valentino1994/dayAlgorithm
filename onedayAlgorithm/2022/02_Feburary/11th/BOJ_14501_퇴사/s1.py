import sys
sys.stdin = open("input.txt", "r")

N = int(input())
schedules = [list(map(int, input().split())) for _ in range(N)]

for i in range(1, len(schedules)):
    tmp = [0]
    for j in range(i):
        if j + schedules[j][0] <= i:
            tmp.append(schedules[j][1])
    if schedules[i][0] + i > N:
        schedules[i][1] = 0
    schedules[i][1] += max(tmp)

result = 0
for i in range(len(schedules)):
    if schedules[i][1] > result:
        result = schedules[i][1]

print(result)