import sys
sys.stdin = open("input.txt")

N = int(input())
n_list = list(map(int, input().split()))

n_list.sort()

left = 0
right = len(n_list)-1
temp = 2000000001 # 최대 덧셈 경우 값(수정 후 성공)
result_a, result_b = n_list[left], n_list[right]

while left < right:
    _sum = n_list[left] + n_list[right]

    if abs(temp) > abs(_sum):
        result_a, result_b = n_list[left], n_list[right]
        temp = _sum

    if _sum > 0:
        right -= 1
    elif _sum < 0:
        left += 1
    else:
        break

print(result_a, result_b)