from pprint import pprint
import sys
sys.stdin = open("input.txt", "r")

N = int(input())
soldiers = list(map(int, input().split()))

IN = [[0] * N for _ in range(N)]

max_value = 0
for i in range(N):
    for j in range(N):
        if i == 0 and soldiers[i] > soldiers[j]:
            IN[i][j] = 1
        else:
            if soldiers[i] > soldiers[j]:
                IN[i][j] = IN[i-1][j] + 1
                if IN[i][j] > max_value:
                    max_value = IN[i][j]
            elif i == j:
                IN[i][j] = 0
            else:
                IN[i][j] = IN[i-1][j]

pprint(N - max_value)