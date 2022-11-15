import sys
sys.stdin = open("input.txt")

N = int(input())
graph = []
for _ in range(N):
    graph.append(list(map(int, input().split(" "))))

sew = []
for i in range(N-1):
    for j in range(i+1, N):
        sew.append([i, j, graph[i][j]])

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

p = list(range(N))
rank = [0] * N

sew.sort(key=lambda x:x[2])

connected_V = 0
i = 0

answer = 0
while connected_V < N and i < len(sew):
    s, e, w = sew[i]
    if find_set(s) != find_set(e):
        union(s, e)
        answer += w
        connected_V += 1
    i += 1

print(answer)
