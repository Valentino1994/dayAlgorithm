import sys
sys.stdin = open("input.txt")

n, x = list(map(int, input().split(" ")))
DP = [0] * (x + 1)
DP[0] = 1

for _ in range(n):
    pipe, cnt = list(map(int, input().split(" ")))
    for l in range(x, -1, -1):
        temp = 0
        for _ in range(cnt):
            temp += pipe
            if l + temp > x:
                break
            # 지금 보는 길이 l에 현재 파이프를 더한 것은 이전 파이프에서 무조건 하나의 수가 생긴 것임으로 경우의 수를 더해줘야함
            DP[l + temp] += DP[l]

print(DP)