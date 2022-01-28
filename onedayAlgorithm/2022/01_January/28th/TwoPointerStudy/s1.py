n = 5
M = 5
arr = [1, 2, 3, 2, 5]

count = 0
interval_sum = 0
end = 0

for start in range(M):

    while interval_sum < M and end < len(arr):
        interval_sum += arr[end]
        end += 1

    if interval_sum == M:
        count += 1

    interval_sum -= arr[start]

print(count)
