import sys
sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
X = int(input())

nums.sort()

count = 0
left, right = 0, N-1

while left < right:

    tmp = nums[left] + nums[right]

    if tmp == X:
        count += 1
    if tmp < X:
        left += 1
        continue

    right -= 1

print(count)
