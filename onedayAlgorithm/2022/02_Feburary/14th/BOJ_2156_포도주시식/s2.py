import sys
sys.stdin = open("input.txt", "r")

N = int(input())
wines = [0]
for _ in range(N):
    wines.append(int(input()))

if N == 1:
    print(wines[0])
else:
    dp = [0] * (N + 1)
    dp[1], dp[2] = wines[1], wines[1] + wines[2]

    for i in range(3, N + 1):
        dp[i] = max(dp[i-1], dp[i-3] + wines[i-1] + wines[i], dp[i-2] + wines[i])

    print(dp[N])

# n = int(input())
# w = [0]
# for i in range(n):
#     w.append(int(input()))
# dp = [0]
# dp.append(w[1])
# if n > 1:
#     dp.append(w[1] + w[2])
# for i in range(3, n + 1):
#     dp.append(max(dp[i - 1], dp[i - 3] + w[i - 1] + w[i], dp[i - 2] + w[i]))
# print(dp[n])

