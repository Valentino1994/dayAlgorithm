import sys
sys.stdin = open("input.txt")

n = int(input())
m = int(input())

tree = []

# 인접행렬 형태로 주어짐
for _ in range(n):
    tree.append(list(map(int, input().split(" "))))

for i in range(n):
    tree[i][i] = 1

def bfs(start: int, end: int):

    visited = [0] * n
    queue = [start]
    queue_index = 0

    result = False

    while queue_index < len(queue):
        node = queue[queue_index]
        for i in range(n):
            if tree[node][i] == 1 and visited[i] == 0:
                visited[i] = 1
                queue.append(i)
                if i == end:
                    return True
        queue_index += 1

    return result

trip_plan = list(map(int, input().split(" ")))

answer = True
for i in range(m-1):
    if not bfs(trip_plan[i]-1, trip_plan[i+1]-1):
        answer = False
        break

if answer:
    print("YES")
else:
    print("NO")



