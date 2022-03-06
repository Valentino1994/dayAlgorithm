import sys
sys.stdin = open("input.txt", "r")
def dfs(pos, min_v):
    ret = 0
    if pos + 1 < len(orders) and orders[pos] > orders[pos + 1]:
        ret += dfs(pos + 1, min(min_v, orders[pos]))
    if pos + ret + 1 < len(orders) and orders[pos] < orders[pos + ret + 1] \
        and orders[pos + ret + 1] < min_v:
        ret += dfs(pos + ret + 1, min_v)
    print(orders[pos])
    return ret + 1

sys.setrecursionlimit(10009)

orders = []
for v in map(int, sys.stdin.read().split()):
    orders.append(v)
dfs(0, 0x3c3c3c3c)