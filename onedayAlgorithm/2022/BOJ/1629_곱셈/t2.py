import sys
sys.stdin = open("input.txt")

A, B, C = list(map(int, input().split(" ")))

def fpow(a, b):
    if b == 1:
        return a
    temp = fpow(a, b//2)
    if b % 2 == 0:
        return temp * temp
    else:
        return a * temp * temp

print(fpow(A, B) % C)