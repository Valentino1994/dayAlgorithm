import sys
sys.stdin = open("input.txt", "r")

N = int(input())
wines = []
for _ in range(N):
    wines.append(int(input()))

max_value = 0
for i in range(N-1, 0, -1):
    wines[i] += wines[i-1]

for i in range(3, N):
    if wines[i-3] + wines[i] > max_value:
        max_value = wines[i-3] + wines[i]
        wines[i] = max_value

print(max_value)