import sys
sys.stdin = open("input.txt", "r")

def make_tree(infos):
    tree = [[-1, [], []] for _ in range(max(infos)+1)]
    root = 0
    now_node = 0
    layer = 1

    for i in range(len(infos)):
        # 첫번째 나오는 건 root노드이다.
        if i == 0:
            root = infos[i]
            tree[root][0] = 0
            continue

        # 1번부터 노드가 시작된다.
        if i == 1:
            now_node = infos[i]
            tree[root][2].append(infos[i])
            tree[infos[i]][1].append(root)
            tree[infos[i]][0] = layer
            continue

        # 현재 보고 있던 노드와 차이가 1이라면 형제이다.
        if infos[i] - now_node == 1:
            layer = tree[now_node][0]
            p = tree[now_node][1][0]
            tree[p][2].append(infos[i])
            tree[infos[i]][1].append(p)
            tree[infos[i]][0] = layer
            now_node = infos[i]

        # 현재 보고 있던 노드와 차이가 1이 넘는다면 자식노드이다.
        else:
            # 먼저 어디에 넣을지 찾는다.
            stack = [root]
            while stack:
                n = stack.pop(0)
                # 자식노드가 없는 곳에 넣는다.
                if not tree[n][2]:
                    layer = tree[n][0] + 1
                    tree[n][2].append(infos[i])
                    tree[n][1].append(n)
                    tree[infos[i]][0] = layer
                    tree[infos[i]][1].append(n)
                    now_node = infos[i]
                    break
                for node in tree[n][2]:
                    stack.append(node)

    return tree

def find_cousin(tree):
    result = 0
    p = tree[k][1][0]
    layer = tree[k][0]

    for t in tree:
        if t[0] == layer and t[1][0] != p:
            result += 1

    return result

while True:
    n, k = list(map(int, input().split()))
    if n == 0 and k == 0:
        break
    infos = list(map(int, input().split()))

    print(find_cousin(make_tree(infos)))
