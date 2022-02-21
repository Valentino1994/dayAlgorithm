import sys
sys.stdin = open("input.txt", "r")

input = sys.stdin.readline
from collections import deque

N, R, Q = map(int, input().split())
infos = [list(map(int, input().split())) for _ in range(N-1)]

# graph를 만들어 Vortex의 정보를 저장한다.
graph = [[[], []] for _ in range(N+1)]
# 연결된 모든 트리를 봐야하기 때문에 양방향으로 만든다.
for info in infos:
    graph[info[0]][0].append(info[1])
    graph[info[1]][0].append(info[0])

level = 1
visited = [False for _ in range(N+1)]
que = deque([R])
visited[R] = True
graph[R][1].append(0)

while que:
    v = que.popleft()
    for i in range(len(graph[v][0])):
        n_v = graph[v][0][i]
        if not visited[n_v]:
            que.append(n_v)
            visited[n_v] = True
            graph[n_v][1].append(level)
    level += 1

for _ in range(Q):

    visited = [False for _ in range(N+1)]

    U = int(input())
    result = 1

    q = deque([U])
    visited[U] = True

    while q:
        vortex = q.popleft()
        now_nodes = graph[vortex][0]
        now_level = graph[vortex][1][0]
        for i in range(len(now_nodes)):
            next_level = graph[now_nodes[i]][1][0]
            if not visited[graph[vortex][0][i]] and now_level < next_level:
                q.append(graph[vortex][0][i])
                result += 1
                visited[graph[vortex][0][i]] = True

    print(result)
