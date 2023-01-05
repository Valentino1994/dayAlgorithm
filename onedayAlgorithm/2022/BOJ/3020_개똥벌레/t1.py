import sys
sys.stdin = open("input.txt")

N, H = list(map(int, input().split(" ")))
cave = []
for _ in range(N):
    cave.append(int(input()))

heights = [0 for _ in range(H)]
for i in range(len(cave)):
    now_height = cave[i]
    if i % 2 == 0:
        for j in range(now_height):
            heights[j] += 1
    else:
        for j in range(H-1, H-now_height-1, -1):
            heights[j] += 1

_min = min(heights)
_count = heights.count(_min)

print(_min, _count)