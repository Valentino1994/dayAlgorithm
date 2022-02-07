N = 4
K = "1 3 1 5"

stores = list(map(int, K.split()))

d = [0] * 101
d[0] = stores[0]
d[1] = max(stores[0], stores[1])

for i in range(2, N):
    d[i] = max(d[i - 1], d[i - 2] + stores[i])

print(d[N-1])