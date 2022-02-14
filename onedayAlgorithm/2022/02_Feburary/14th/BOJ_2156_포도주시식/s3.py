import sys
sys.stdin = open("input.txt", "r")

N = int(input())
wines = [int(input()) for _ in range(N)]

a, b, c = 0, 0, 0
for wine in wines:
    a, b, c = max(a, b, c), a + wine, b + wine

print(max(a, b, c))