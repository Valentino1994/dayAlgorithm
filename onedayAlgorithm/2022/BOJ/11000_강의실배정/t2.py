import sys
sys.stdin = open("input.txt")

import heapq

N = int(input())
Time = []
heap = []

for _ in range(N):
    S, T = list(map(int, input().split(" ")))
    Time.append([S, T])

Time = sorted(Time, key=lambda x: (x[0], x[1]))

heapq.heappush(heap, Time[0][1])
for i in range(1, N):
    if Time[i][0] < heap[0]:
        heapq.heappush(heap, Time[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, Time[i][1])

print(len(heap))
