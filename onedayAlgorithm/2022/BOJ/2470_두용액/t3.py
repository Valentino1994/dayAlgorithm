import sys
sys.stdin = open("input.txt")

n = int(input())
liquids = list(map(int, input().split(" ")))
liquids.sort()

center = n // 2

candidate1 = liquids[center] + liquids[center + 1]
candidate2 = liquids[center] + liquids[center - 1]
candidate3 = liquids[0] + liquids[-1]

amount = 1000000000
answer = []
if abs(candidate1) < amount:
    amount = abs(candidate1)
    answer.append((liquids[center], liquids[center + 1]))
if abs(candidate2) < amount:
    amount = abs(candidate2)
    answer.append((liquids[center], liquids[center - 1]))
if abs(candidate3) < amount:
    amount = abs(candidate3)
    answer.append((liquids[0], liquids[-1]))

answer.sort(key=lambda x:abs(x[0] + x[1]))
print(answer[0])