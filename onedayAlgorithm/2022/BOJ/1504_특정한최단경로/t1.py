import sys
sys.stdin = open("input.txt")

N, M = list(map(int, input().split(" ")))
edges = []

for _ in range(M):
    edges.append(list(map(int, input().split(" "))))

V1, V2 = list(map(int, input().split(" ")))

# MST 만들기
def find_set(x):
    if p[x] != x:
        return find_set(p[x])
    else:
        return p[x]

def union(x, y):
    a = find_set(x)
    b = find_set(y)

    if a == b:
        return
    elif rank[a] < rank[b]:
        p[b] = a
    elif rank[a] > rank[b]:
        p[a] = b
    else:
        p[a] = b
        rank[b] += 1

p = list(range(N+1))
rank = [0] * (N+1)

connected_V = 0
i = 0

# index == node, 0 == child, 1 == weight
mst = [ [] for _ in range(N+1) ]
edges.sort(key=lambda x:x[2])

while connected_V < N and i < M:
    s, e, w = edges[i]
    if find_set(s) != find_set(e):
        union(s, e)
        connected_V += 1
        mst[s].append([e, w])
        mst[e].append([s, w])
    i += 1

def dijkstra(s, e):
    # s에서 e로 가는 최단 경로의 가중치들을 구해서 answer에 더해줌.
    result = 0
    V = [987654321] * (N+1)
    queue = [s]
    queue_index = 0
    V[s] = 0
    while len(queue) > queue_index:
        nodes = queue[queue_index]
        for node in mst[nodes]:
            c, w = node
            # V[c]는 현재 c까지 가는 최단 경로를 저장해둔 것.
            if V[c] > V[nodes] + w:
                V[c] = V[nodes] + w
            queue.append(c)
            if c == e:
                result = V[c]
                return result

        queue_index += 1

answer = 0
route = [1, V1, V2, N]
for i in range(len(route)-1):
    answer += dijkstra(route[i], route[i+1])

print(answer)

