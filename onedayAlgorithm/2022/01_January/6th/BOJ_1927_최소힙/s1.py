import sys
import heapq

# 백준에서는 항상 이걸 쓰자.
input = sys.stdin.readline
N = int(input())

q = []
for i in range(N):
    case = int(input())
    if case == 0:
        if q:
            print(heapq.heappop(q))
        else:
            print(0)
    else:
        heapq.heappush(q, case)