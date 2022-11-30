import sys
import pprint
sys.stdin = open("input.txt")

N, M = list(map(int, input().split(" ")))
maze = []

for _ in range(N):
    int_array = []
    now_strings = input()
    for now_string in now_strings:
        int_array.append(int(now_string))
    maze.append(int_array)

# 항상 도착할 수 있음
queue = [(0, 0)]
queue_index = 0

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

now_time = 1
maze[0][0] = 0
while queue_index < len(queue):
    now_row, now_column = queue[queue_index]
    for i in range(4):
        next_row = now_row + dr[i]
        next_column = now_column + dc[i]

        if 0 <= next_row < N and 0 <= next_column < M and maze[next_row][next_column] != 0 and (next_row, next_column) not in queue:
            queue.append((next_row, next_column))
            maze[next_row][next_column] = min(maze[now_row][now_column] + 1, queue_index+1)

    queue_index += 1

print(maze[N-1][M-1] + 1)