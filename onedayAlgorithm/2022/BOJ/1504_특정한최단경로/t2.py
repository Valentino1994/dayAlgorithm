import heapq
from sys import stdin

INF = int(1e9)
N, E = map(int, stdin.readline().split())
graph = [[] for i in range(N + 1)]
for i in range(E):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

def dijkstra(start, end):
    heap = []
    board = [INF for i in range(N + 1)]
    board[start] = 0
    heapq.heappush(heap, (0, start))
    while heap:
        # 현재 노드로 가는 weight
        weight, node = heapq.heappop(heap)
        if weight > board[node]: continue                       # 현재 노드에 저장된 weight가 더 작으면 넘어감.
        for w, next_node in graph[node]:                        # 현재 노드에서 갈 수 있는 모든 노드를 보면서
            if w + weight < board[next_node]:                   # 다음으로 갈 수 있는 노드에 현재 저장된 값이 현재 노드 + 현재 길의 weight보다 크면 진행시킴
                board[next_node] = w + weight                   # 다음 노드에 넣고
                heapq.heappush(heap, (w + weight, next_node))   # heap에 넣는다.
    return board[end]

routes = list(map(int, stdin.readline().split()))
result = min(dijkstra(1, routes[0]) + dijkstra(routes[0], routes[1]) + dijkstra(routes[1], N),
             dijkstra(1, routes[1]) + dijkstra(routes[1], routes[0]) + dijkstra(routes[0], N))
print("-1" if result >= INF else result)