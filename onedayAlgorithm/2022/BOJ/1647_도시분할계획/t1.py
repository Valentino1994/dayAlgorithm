import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

def find_set(x):
    if p[x] != x:
        return find_set(p[x])
    else:
        return p[x]

def union(a, b):
    # p[find_set(a)] = find_set(b) 요걸 아래처럼 최적화 할 수 있음
    a = find_set(a)
    b = find_set(b)

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
edges = []
for _ in range(E):
    edges.append(list(map(int, input().split(" "))))

edges.sort(key = lambda x:x[2])

p = list(range(V+1))
rank = [0] * (V+1)
connected_V = 0
i = 0
answer = 0
end = 0
while connected_V < V and i < E:
    s, e, w = edges[i]
    if find_set(s) != find_set(e):
        union(s, e)
        connected_V += 1
        answer += w
        end = w
    i += 1

print(answer - end)