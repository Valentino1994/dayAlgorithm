import sys
sys.stdin = open("input.txt", "r")
# input = sys.stdin.readline

T = int(input())
for _ in range(T):
    cnt = 1
    N = int(input())
    ranks = [list(map(int, input().split())) for _ in range(N)]
    ranks.sort()
    compare_target = ranks[0]
    for i in range(1, N):
        if (ranks[i][1] < compare_target[1]):
            cnt += 1
            compare_target = ranks[i]

    print(cnt)