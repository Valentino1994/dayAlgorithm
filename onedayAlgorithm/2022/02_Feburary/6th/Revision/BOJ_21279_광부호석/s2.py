import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, C = map(int, input().split())
# y좌표를 인덱스로 x좌표들을 저장
minerals = [[] for _ in range(100001)]
# x축의 실시간 y까지 광물 가치
x_values = [0 for _ in range(100001)]
# x축의 광물 개수(캐는 비용)
x_cost = [0 for _ in range(100001)]

for _ in range(N):
    x, y, v = map(int, input().split())
    minerals[y].append((x, v))
y = 0
money = 0
ans = 0
cnt = 0
for x in range(100000, -1, -1):

    while y <= 100000 and cnt < C:
        # y축 경계선에 있는 광물들의 광물가격과 비용을 x축 리스트에 추가해준다.
        for x2, v in minerals[y]:
            if x2 <= x:
                money += v
                cnt += 1

                x_values[x2] += v
                x_cost[x2] += 1
        y += 1

    # 현재 비용이 초과하지 않은 경우
    if cnt <= C:
        ans = max(ans, money)

    # 현재 x축에 해당하는 광물가격과 비용을 빼준다.
    money -= x_values[x]
    cnt -= x_cost[x]
print(ans)