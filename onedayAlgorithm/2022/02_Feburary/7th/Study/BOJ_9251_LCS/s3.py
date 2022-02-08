import sys
sys.stdin = open("input.txt", "r")

str1 = input()
str2 = input()

dp = [0 for i in range(len(str2) + 1)]

for i in range(1, len(str1) + 1):
    cnt = 0
    for j in range(1, len(str2) + 1):
        if cnt < dp[j]:
            cnt = dp[j]

        elif str1[i - 1] == str2[j - 1]:
            dp[j] = cnt + 1
print(dp)
print(max(dp))