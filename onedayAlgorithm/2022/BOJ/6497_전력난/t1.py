import sys
sys.stdin = open("input.txt")

input = sys.stdin.readline

def find_set(x):
    if p[x] != x:
        return find_set(p[x])
    else:
        return p[x]

def union(s, e):
    a = find_set(s)
    b = find_set(e)

    if a < b:
        p[b] = a
    else:
        p[a] = b

while True:
    V, E = list(map(int, input().split()))

    if V == 0 and E == 0:
        break

    edges = []
    for _ in range(E):
        edges.append(list(map(int, input().split())))

    p = list(range(V + 1))

    connected_V = 0
    i = 0
    answer = 0
    edges.sort(key=lambda x: x[2])

    while connected_V < V and i < E:
        s, e, w = edges[i]
        if find_set(s) != find_set(e):
            union(s, e)
            connected_V += 1
        else:
            answer += w

        i += 1

    print(answer)