import sys
sys.stdin = open("input.txt")

n = int(input())
tree = [[] for _ in range(n)]

for _ in range(n-1):
    p, c = list(map(int, input().split(" ")))
    tree[p-1].append(c-1)
    tree[c-1].append(p-1)

# 1번 인덱스를 루트노드라고 할 때 부모 노드를 찾는 법. -> BFS를 돌면서 여기서 갈 수 있는 애는 해당 노드를 넣어준다.
queue = [0]
queue_index = 0
visited = [0 for _ in range(n)]
answer = ""
while queue_index < len(queue):
    node = queue[queue_index]
    now_nodes = tree[node]
    for next_node in now_nodes:
        if visited[next_node] == 0:
            visited[next_node] = node + 1
            queue.append(next_node)
    queue_index += 1

for i in range(1, n):
    print(visited[i])