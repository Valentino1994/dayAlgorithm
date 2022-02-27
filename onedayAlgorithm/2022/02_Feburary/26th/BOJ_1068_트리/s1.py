import sys
sys.stdin = open("input.txt", "r")

N = int(input())
nodes = list(map(int, input().split()))
cancel_node = int(input())

tree = [[] for _ in range(N)]

for i, node in enumerate(nodes):
    if node == -1:
        continue
    tree[node].append(i)

p = nodes[cancel_node]
if cancel_node in tree[p]:
    tree[p].remove(cancel_node)

c_stack = [cancel_node]
while c_stack:
    c = c_stack.pop()
    for i in range(len(tree[c])):
        c_stack.append(tree[c][i])
    tree[c] = []

result = 0
root = 987654321
for i in range(len(nodes)):
    if nodes[i] != -1 and root > nodes[i]:
        root = nodes[i]

stack = [root]

while stack:
    n = stack.pop()
    for vortex in tree[n]:
        if not tree[vortex]:
            result += 1
        else:
            stack.append(vortex)

print(result)