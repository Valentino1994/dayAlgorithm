import sys
sys.stdin = open("input.txt")

n, x = list(map(int, input().split(" ")))
DP = [0] * (x+1)
DP[0] = 1

for i in range(n):
    pipe, c = list(map(int, input().split(" ")))
    for length in range(x, -1, -1):
        temp = 0
        for j in range(c):
            temp += pipe
            if length + temp > x:
                break
            # 지금 보는 파이프의 개수로 만들 수 있는 길이 = 이전 파이프의 개수로 만들 수 있는 길이를 더한 것
            DP[length + temp] += DP[length]

print(DP[x])