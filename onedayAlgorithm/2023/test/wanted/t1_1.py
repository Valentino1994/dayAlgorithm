import sys
sys.stdin = open("input1.txt")

N = int(input())
states = list(map(int, input().split(" ")))

answer = 0

visited = []
now_direction = states[0]
temp = 1
for i in range(N):
    if states[i] == now_direction:
        if now_direction == 1:
            temp += 1
        else:
            temp -= 1
    else:
        visited.append(temp)
        temp = 1

print(visited)
print(max(visited))
