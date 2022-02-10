import sys
sys.stdin = open("input.txt", "r")

N, T, P = map(int, input().split())
tmp_times = [list(input().split()) for _ in range(T)]
times = []
tables = [[[0, 0]] for _ in range(N)]

# 먼저 시간 계산을 편하게 하기 위해 분 단위로 다 바꿔주고 시작 시간 순으로 정렬한다.(일찍 온 사람이다.)
for tmp_time in sorted(tmp_times):
    tmp = []
    for i in range(2):
        hour = int(tmp_time[i][0:2])
        minute = int(tmp_time[i][2:5])
        tmp.append(hour * 60 + minute)
    times.append(tmp)

# 시간을 돌면서 그 사람이 선호하는 자리에 시간을 넣는다.
for time in times:
    # 선호도 순으로 좌석을 돌면서 비었는지 확인한다.
    # 1순위 0번 자리, 0번 자리의 최근 앉은 사람의 끝나는 시간이 현재 사람보다 더 크다면,
    if tables[0][-1][1] <= time[0]:
        tables[0].append(time)
    # 2순위 끝자리, N번 자리의 최근 앉은 사람의 끝나는 시간이 현재 사람보다 더 크다면,
    elif tables[N-1][-1][1] <= time[0]:
        tables[N-1].append(time)
    # 그게 아니라면 더 넓은 공간을 찾고 그 공간에서 가운데를 찾는다.
    else:
        now, tmp = [0] * 3, [0] * 3
        for i in range(1, len(tables)):
            if tables[i][-1][1] <= time[0]:
                tmp[0] += 1
                if tmp[0] == 1:
                    tmp[1] = i
                tmp[2] = i
            else:
                if tmp[0] > now[0]:
                    now = tmp
                tmp = [0] * 3
        idx = N // 2 - 1 if N % 2 == 0 else N // 2
        tables[idx].append(time)

result = 720
for t in tables[P-1]:
    result -= (t[1] - t[0])

print(result)
# P 자리에 사람이 앉아 있던 시간을 720분에서 뺀다.