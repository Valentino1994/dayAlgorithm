import sys
sys.stdin = open("input.txt", "r")

string = input().split('-')

nums = []
for s in string:
    cnt = 0
    isPlus = s.split('+')
    for num in isPlus:
        cnt += int(num)
    nums.append(cnt)

result = nums[0]
for i in range(1, len(nums)):
    result -= nums[i]

print(result)