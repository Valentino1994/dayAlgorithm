import sys
sys.stdin = open("input.txt", "r")
from itertools import combinations

N = int(input())
tree = [[[], [], []] for _ in range(N+1)]
for _ in range(N):
    info = list(map(int, input().split()))
    p = info[0]
    for i in range(1, len(info)-1, 2):
        c = info[i]
        d = info[i+1]
        if p not in tree[c][0] and c not in tree[p][1]:
            tree[p][1].append(c)
            tree[p][2].append(d)
            tree[c][0].append(p)

leaf = []
for i in range(len(tree)):
    if len(tree[i][0]) == 1:
        leaf.append(i)

distance = 0
def find_distance(root):

    global distance

    tmp = 0
    q = [root]

    return

print(tree)
print(leaf)

