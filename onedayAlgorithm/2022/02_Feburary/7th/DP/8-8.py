n, m = 2, 15
array = [2, 3]

d = [1001] * (m + 1)

d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 1001:
            d[j] = min(d[j], d[j - array[i]] + 1)

if d[m] == 1001:
    print(-1)
else:
    print(d[m])