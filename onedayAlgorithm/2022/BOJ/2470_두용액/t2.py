import sys
sys.stdin = open("input.txt")

n = int(input())
liquids = list(map(int, input().split(" ")))
liquids.sort()

amount = 1000000000
answer = []

def check(mixing_liquid, base_liquid, i, j):
    global amount
    if amount > abs(mixing_liquid + base_liquid):
        amount = abs(mixing_liquid + base_liquid)
        answer.append((liquids[i], liquids[j]))

for i in range(n//2 + 1):
    if i == n//2:
        base_liquid = liquids[i]
        mixing_liquid = liquids[i+1]
        check(mixing_liquid, base_liquid, i, i+1)
    else:
        base_liquid = liquids[i]
        mixing_liquid = liquids[n-i-1]
        check(mixing_liquid, base_liquid, i, n-i-1)

print(answer[-1])

