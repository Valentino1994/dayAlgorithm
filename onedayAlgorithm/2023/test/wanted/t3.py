import sys
sys.stdin = open("input3.txt")

N, M, C = list(map(int, input().split(" ")))
W = []
for _ in range(C):
    W.append(list(map(int, input().split(" "))))

A = list(map(int, input().split(" ")))
B = list(map(int, input().split(" ")))

