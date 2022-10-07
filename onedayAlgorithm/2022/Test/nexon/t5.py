import heapq
import sys

def minCostPath(g_nodes, g_from, g_to, g_weight, x, y):
    # Write your code here
    INF = int(1e9)

    # list for connecting information between nodes
    graph = [[] for i in range(g_nodes + 1)]
    # table for shortest path
    distance = [INF] * (g_nodes + 1)

    for _ in range(len(g_from)):
        a, b, c = g_from, g_to, g_weight
        graph[a].append((b, c))

    def dijkstra(start):
        q = []
        # set starting node distance as 0
        heapq.heappush(q, (0, start))
        distance[start] = 0

        while q:  # while queue is not empty
            # get the shorttest node
            dist, now = heapq.heappop(q)

            # continue if already processed node
            if distance[now] < dist:
                continue
            # check near nodes
            for i in graph[now]:
                cost = dist + i[1]
                # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

        # run dijkstra
        dijkstra(start)

        # print the shortest distances
        for i in range(1, g_nodes + 1):
            # if not reachable, print INF
            if distance[i] == INF:
                print("INF")
            # print reachable distance
            else:
                print(distance[i])