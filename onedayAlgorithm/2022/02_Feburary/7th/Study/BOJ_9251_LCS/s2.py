import sys
sys.stdin = open("input.txt", "r")
#input = sys.stdin.readline
X = input().rstrip()
Y = input().rstrip()


DP = [0] * 1000

for i, x in enumerate(X):
    cnt = 0
    for j, y in enumerate(Y):
        if cnt < DP[j]:
            cnt = DP[j]
        elif x == y:
            DP[j] = cnt + 1

print(DP)
print(max(DP))