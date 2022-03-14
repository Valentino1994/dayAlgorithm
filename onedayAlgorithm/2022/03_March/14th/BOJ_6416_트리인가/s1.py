import sys
sys.stdin = open("input.txt", "r")

def treeDefine(nodes):
    tree = [[[],[]] for _ in range(100000)]
    for i in range(0, len(nodes)-1, 2):
        p = nodes[i]
        c = nodes[i+1]
        tree[c][0].append(p)
        tree[p][1].append(c)

    for node in tree:
        if len(node[0]) > 1:
            return False

    return True

case = 0
while True:
    case += 1
    nodes = []
    flag = False
    while True:
        inp = list(map(int, input().split()))
        if inp == [-1, -1]:
            flag = True
            break

        if inp[-2:] == [0, 0]:
            nodes.extend(inp)
            define = treeDefine(nodes)
            if define:
                print("Case {} is a tree.".format(case))
            else:
                print("Case {} is not a tree.".format(case))
            break

        else:
            nodes.extend(inp)

    if flag:
        break