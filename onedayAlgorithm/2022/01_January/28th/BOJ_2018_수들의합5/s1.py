import sys
sys.stdin = open("input.txt", "r")

#input = sys.stdin.readline

N = int(input())

count = 0
interval_sum = 0
end = 0

numbers = range(1, N+1)

for start in range(N):

    while interval_sum < N and end < N:
        interval_sum += numbers[end]
        end += 1

    if interval_sum == N:
        count += 1

    interval_sum -= numbers[start]

print(count)
