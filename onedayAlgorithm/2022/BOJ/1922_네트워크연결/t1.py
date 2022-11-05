import sys
sys.stdin = open("input.txt")


def find_set(x): # 루트 노드 찾기
    if x != p[x]:
        return find_set(p[x])
    else:
        return x

def union(x, y): # 루트 노드 잇기
    p[find_set(y)] = find_set(x) # y의 루트를 x의 루트로 지정

V = int(input())
E = int(input())

graph = [[0] * (V+1) for _ in range(V+1)]
edges = []

for _ in range(E):
    s, e, w = map(int, input().split(" "))
    graph[s][e] = w
    graph[e][s] = w
    edges.append([s, e, w])

edges.sort(key = lambda x : x[2])
p = list(range(V+1))

connected_edges = 0
min_cost = 0

i = 0
while connected_edges < V and i < E:
    s, e, w = edges[i]

    if find_set(s) != find_set(e):
        print(s, e, w)
        print(p)
        union(s, e)
        print(p)
        connected_edges += 1
        min_cost += w

    i += 1

print(min_cost)