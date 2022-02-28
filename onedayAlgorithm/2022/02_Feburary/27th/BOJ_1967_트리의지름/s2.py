import sys
# input = sys.stdin.readline
sys.stdin = open("input.txt", "r")

n = int(input())
adj = [[] for _ in range(n+1)]
ans = [(0, 0)] * (n+1)
for _ in range(n-1):
    p, c, w = map(int, input().rstrip().split())
    adj[p].append((c, w))
for i in range(n, 0, -1):
    mx, mx2 = 0, 0
    for v, w in adj[i]:
        t = w + ans[v][0]
        if t > mx:
            mx2 = mx
            mx = t
        elif t > mx2:
            mx2 = t
    ans[i] = (mx, mx2)
ans.sort(reverse = True, key = lambda x: sum(x))
print(sum(ans[0]))