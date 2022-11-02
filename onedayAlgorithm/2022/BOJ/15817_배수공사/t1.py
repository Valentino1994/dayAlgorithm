import sys
sys.stdin = open("input.txt")
from pprint import pprint
# input = sys.stdin.readline

n, x = map(int, input().split())
dp = [0] * (x + 1)
dp[0] = 1

for i in range(n):
    l, c = map(int, input().split())

    for j in range(x, -1, -1):
        temp = 0
        for k in range(c):
            temp += l
            if j + temp > x:
                break
            dp[j + temp] += dp[j]

print(dp)
print(dp[x])