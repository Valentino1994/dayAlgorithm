import sys
from collections import defaultdict

sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline

N = int(input())

A, B, C, D = [], [], [], []
tmp = [ list(map(int, input().split())) for _ in range(N) ]

for t in tmp:
    for i in range(4):
        if i == 0:
            A.append(t[i])
        elif i == 1:
            B.append(t[i])
        elif i == 2:
            C.append(t[i])
        else:
            D.append(t[i])

AB = defaultdict(int)
for i in range(N):
    for j in range(N):
        ab = A[i] + B[j]
        AB[ab] += 1

result = 0
for i in range(N):
    for j in range(N):
        cd = -(C[i] + D[j])
        if cd in AB:
            result += AB[cd]
print(AB)