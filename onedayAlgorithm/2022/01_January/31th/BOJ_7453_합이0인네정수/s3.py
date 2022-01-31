import sys
sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline

n = int(input())
A, B, C, D = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)

AB = []
for a in A:
    for b in B:
        AB.append(a+b)
CD = []
for c in C:
    for d in D:
        CD.append(c+d)
AB.sort()
CD.sort()
ans = 0

i = 0
j = n*n-1
while i < n*n and 0 <= j:
    temp = AB[i] + CD[j]
    if temp == 0:
        a, b = i, j
        i, j = i+1, j-1
        while i < n*n and AB[i] == AB[i-1]:
            i += 1
        while j >= 0 and CD[j] == CD[j+1]:
            j -= 1
        ans += (i-a) * (b-j)
    elif temp > 0:
        j -= 1
    elif temp < 0:
        i += 1

print(ans)