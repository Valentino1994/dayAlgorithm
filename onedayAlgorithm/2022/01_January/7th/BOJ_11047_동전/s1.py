import sys
sys.stdin = open("input.txt", "r")

N, K = map(int, input().split())
p = []
for _ in range(N):
    p.append(int(input()))

new_p = p[::-1]

answer = 0

for coin in new_p:

    if K / coin < 0:
        continue

    answer += K // coin
    K = K % coin

print(answer)