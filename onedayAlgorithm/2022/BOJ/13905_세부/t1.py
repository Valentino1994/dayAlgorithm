import sys
sys.stdin = open("input.txt")
# input = sys.stdin.readline

def find_set(x):
    if p[x] != x:
        return find_set(p[x])
    else:
        return p[x]

def union(x, y):
    a = find_set(x)
    b = find_set(y)

    # 이미 부모가 같다면 리턴
    if a == b:
        return
    # union을 최적화하는 것
    if rank[a] > rank[b]:
        p[b] = a
    elif rank[a] < rank[b]:
        p[a] = b
    else:
        p[a] = b
        rank[b] += 1


V, E = list(map(int, input().split(" ")))
A, B = list(map(int, input().split(" ")))

edges = []

for _ in range(E):
    edges.append(list(map(int, input().split(" "))))

p = list(range(V + 1))
tree = [[0] * (V+1) for _ in range(V+1)]
rank = [0] * (V+1)

edges.sort(key = lambda x:x[2], reverse=True)

connected_V = 0
i = 0
while connected_V < V and i < E:
    s, e, w = edges[i]

    if find_set(s) != find_set(e):
        union(s, e)
        connected_V += 1
        tree[s][e] = w

    i += 1

answer = 987654321
queue = [B]
queue_index = 0
while queue_index < len(queue):
    node = queue[queue_index]
    now = tree[node]

    if node == A:
        break

    for i in range(len(now)):
        if now[i] != 0:
            answer = min(answer, now[i])
            queue.append(i)

    queue_index += 1


print(answer)