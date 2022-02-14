import sys
sys.stdin = open("input.txt", "r")

N, K = map(int, input().split())
print(N, K)

if K == 1:
    print(N)
else:
    dp = [0] * (N + 1)
    dp[K] = 1
    for i in range(K+1, N + 1):
        pass
    print(dp)