import sys
sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline

N = int(input())
arr = [0] * (N + 1)
for _ in range(N - 1):
    s, e = map(int, input().split())
    arr[s] += 1
    arr[e] += 1

M = int(input())
for _ in range(M):
    flag = False
    q, v = map(int, input().split())
    if q == 1:
        if arr[v] > 1:
            flag = True
    else:
        flag = True

    if flag:
        print("yes")
    else:
        print("no")