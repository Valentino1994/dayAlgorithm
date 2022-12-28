import sys
sys.stdin = open("input.txt")

n = int(input())
liquid = list(map(int, input().split(" ")))

amount = 1000000000
answer = []
for i in range(n):
    base_liquid = liquid[i]
    for j in range(i, n):
        mixing_liquid = liquid[j]
        if amount > abs(mixing_liquid + base_liquid):
            amount = abs(mixing_liquid + base_liquid)
            answer.append((liquid[i], liquid[j]))

print(answer[-1])