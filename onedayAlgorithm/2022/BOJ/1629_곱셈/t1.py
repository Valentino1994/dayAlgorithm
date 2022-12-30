import sys
sys.stdin = open("input.txt")

A, B, C = list(map(int, input().split(" ")))

answer = A ** B

print(answer % C)