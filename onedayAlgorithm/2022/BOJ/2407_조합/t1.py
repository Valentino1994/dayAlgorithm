import sys
sys.stdin = open("input.txt")
import math

N, R = list(map(int, input().split(" ")))

mother = math.factorial(N)
child = math.factorial(R) * math.factorial(N - R)

print(mother // child)