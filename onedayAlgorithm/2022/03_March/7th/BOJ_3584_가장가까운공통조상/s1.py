import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def find_parent(node):
    stack = [node]
    parent = [node]
    while stack:
        n = stack.pop()
        if tree[n][0]:
            stack.append(tree[n][0][0])
            parent.append(tree[n][0][0])
    return parent

def find_common(p1, p2):
    min_parent = p1 if len(p1) <= len(p2) else p2
    other = p2 if len(p1) >= len(p2) else p1
    for i in range(len(min_parent)):
        if min_parent[i] in other:
            return min_parent[i]

for _ in range(T):
    # 0은 부모노드 1은 자식노드
    N = int(input())
    tree = [[[], []] for _ in range(N + 1)]

    for _ in range(N-1):
        P, C = map(int, input().split())
        tree[P][1].append(C)
        tree[C][0].append(P)
    A, B = map(int, input().split())

    result = find_common(find_parent(A), find_parent(B))
    print(result)

