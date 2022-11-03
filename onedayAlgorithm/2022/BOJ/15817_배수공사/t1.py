import sys
sys.stdin = open("input.txt")
from pprint import pprint
# input = sys.stdin.readline

n, x = map(int, input().split())
dp = [0] * (x + 1)
dp[0] = 1

for i in range(n):
    # 길이 개수
    l, c = map(int, input().split())
    # 무게를 뒤부터 봄 -> WHY ?
    for j in range(x, -1, -1):
        temp = 0
        # 파이프 개수
        for k in range(c):
            temp += l
            # 무게 넘어가면 안봄
            if j + temp > x:
                break
            # dp[j]
            dp[j + temp] += dp[j]

print(dp)
print(dp[x])