import sys
sys.stdin = open("input.txt", "r")

nums = range(1, 13)

def SubsetSum():
    result = 0
    for i in range(1 << len(nums)):
        total = 0
        cnt = 0
        for j in range(len(nums)):
            if i & (1 << j):
                total += nums[j]
                cnt += 1
        if cnt == N and total == K:
            result += 1
    return result

T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    print("#{} {}".format(tc, SubsetSum()))