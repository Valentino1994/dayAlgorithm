import sys
sys.stdin = open("input.txt", "r")

n = int(input())
# 0: parent node, 1: child node 2: child node 까지의 가중치
tree = [[[],[],[0]*13] for _ in range(n + 1)]
try:
    for _ in range(n):
        info = list(map(int, input().split()))
        p, c, e = info[0], info[1], info[2]
        tree[p][1].append(c)
        tree[p][2][c] = e
        tree[c][0].append(p)
except:
    pass

leaf_nodes = []
for i in range(2, n + 1):
    # 부모 노드가 있는데 자식 노드가 없다면 리프 노드
    if tree[i][0] and not tree[i][1]:
        leaf_nodes.append(i)

def find_parent(node):
    parents = []
    stack = [tree[node][0][0]]
    # 루트 노드의 번호는 항상 1임으로 루트노드까지 간다.
    while stack[0] != 1:
        next_parent = stack.pop()
        parents.append(next_parent)
        if tree[next_parent][0][0]:
            stack.append(tree[next_parent][0][0])
    parents.append(1)
    return parents

def sum_edges(node):
    result = 0
    stack = [node]
    while True:
        now = stack.pop()
        if now == 1:
            break
        p = tree[now][0][0]
        result += tree[p][2][now]
        stack.append(p)

    return result
answer = 0
# 노드와 노드 간의 거리는 root에서 leaf_node1까지의 가중치 + leaf_node2까지의 가중치 - 2 * (root에서 공통된 부모 노드까지 갈 때의 가중치)
for i in range(len(leaf_nodes)):
    for j in range(i, len(leaf_nodes)):
        n1, n2 = leaf_nodes[i], leaf_nodes[j]
        if n1 == n2:
            continue
        n1_parents = find_parent(n1)
        n2_parents = find_parent(n2)
        how = max(len(n1_parents), len(n2_parents))
        common = 0
        for k in range(how):
            if n1_parents[k] == n2_parents[k]:
                common = n1_parents[k]
                break
        if common == 1:
            tmp = sum_edges(n1) + sum_edges(n2)
        else:
            tmp = sum_edges(n1) + sum_edges(n2) - (2 * sum_edges(common))
        if tmp > answer:
            answer = tmp

print(answer)
