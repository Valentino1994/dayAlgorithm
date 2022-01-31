import sys
from itertools import permutations
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

cnt = 0
for p in permutations(range(N), 4):
    a, b, c, d = p[0], p[1], p[2], p[3]
    if (A[a] + B[b] + C[c] + D[d]) == 0:
        cnt += 1
    print(a, b, c, d)
    print(A[a], B[b], C[c], D[d])
    print(A[a] + B[b] + C[c] + D[d])

print(cnt)
