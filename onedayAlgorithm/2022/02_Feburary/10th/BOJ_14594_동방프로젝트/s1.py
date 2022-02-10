import sys
sys.stdin = open("input.txt", "r")

N = int(input())
M = int(input())
villains = [list(map(int, input().split())) for _ in range(M)]

rooms = [0]
for i in range(1, N+1):
    rooms.append(i)

for villain in villains:
    x, y = villain
    if x < y:
        room_num = rooms[x]
        for i in range(x, y + 1):
            rooms[i] = room_num
result = 1
for i in range(2, N+1):
    if rooms[i-1] != rooms[i]:
        result += 1

print(result)