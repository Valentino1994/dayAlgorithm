import sys
sys.stdin = open("input.txt", "r")

# node가 몇개인지 안가르쳐줌
nodes = []
while True:
    try:
        nodes.append(int(input()))
    except:
        break
# tree를 먼저 다시 그린다.
tree = [[0, 0, 0] for _ in range(len(nodes))]
now_root = 0
for i, node in enumerate(nodes):
    tree[i][0] = node
    if i == 0:
        continue
    if node < tree[now_root][0]:
        tree[now_root][1] = i
        now_root = i
    elif node > tree[now_root][0]:
        if now_root == 0:
            tree[now_root][2] = i
            now_root = i
            continue
        while tree[now_root][0] < node:
            now_root -= 1
        tree[now_root + 1][2] = i

def recursion(node):
    if tree[node][1] == 0 and tree[node][2] == 0:
        print(tree[node][0])
        return
    if tree[node][1]:
        recursion(tree[node][1])
    if tree[node][2]:
        recursion(tree[node][2])
    print(tree[node][0])
recursion(0)

print(tree)