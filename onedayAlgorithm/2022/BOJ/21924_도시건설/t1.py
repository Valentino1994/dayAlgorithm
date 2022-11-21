import sys
sys.stdin = open("input.txt")

V, E = list(map(int, input().split(" ")))
edges = []

now_sum = 0
for _ in range(E):
    s, e, w = list(map(int, input().split(" ")))
    now_sum += w
    edges.append([s, e, w])

def find_set(x):
    if p[x] != x:
        return find_set(p[x])
    else:
        # root가 같은 건지 확인하는 것
        return p[x]

def union(x, y):
    a = find_set(x)
    b = find_set(y)

    if a == b:
        return
    if rank[a] < rank[b]:
        p[b] = a
    elif rank[a] > rank[b]:
        p[a] = b
    else:
        p[a] = b
        rank[b] += 1

p = list(range(V+1))
rank = [0] * (V+1)

edges.sort(key = lambda x:x[2])
connected_V = 0
i = 0

shortest_way = 0
while connected_V < V and i < len(edges):
    s, e, w = edges[i]
    if find_set(s) != find_set(e):
        union(s, e)
        connected_V += 1
        shortest_way += w
    i += 1

for i in range(1, V+1):
    a = find_set(i)
    if a != p[i]:
        p[i] = a

def check_connected(p):
    flag = p[1]
    for i in range(2, len(p)):
        if flag != p[i]:
            return False
    return True

answer = (now_sum - shortest_way) if check_connected(p) else -1
print(answer)
