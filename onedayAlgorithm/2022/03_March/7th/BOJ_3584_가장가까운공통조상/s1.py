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

    if len(p1) < len(p2):
        min_parent = p1
        other = p2
    else:
        min_parent = p2
        other = p1

    pre = p1[-1]
    for i in range(len(min_parent)-1, -1, -1):
        if i == 0:
            return min_parent[0]
        if min_parent[i] in other:
            pre = min_parent[i]
        else:
            return pre

    # 뒤 부터 탐색 무조건 root 노드부터 이기 때문에
    # pre = 0
    # for a, b in zip(p1[::-1], p2[::-1]):
    #     if a == b:
    #         pre = a
    #     else:
    #         return pre
    #         break
    # else:
    #     return pre

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
    # print(find_parent(A), find_parent(B))
    print(result)

