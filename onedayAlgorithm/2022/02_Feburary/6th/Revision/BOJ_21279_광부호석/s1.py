import sys
sys.stdin = open("input.txt", "r")
#input = sys.stdin.readline

N, C = map(int, input().split())
Xs = []
Ys = []
Pairs = []
for _ in range(N):
    X, Y, V = map(int, input().split())
    Xs.append(X)
    Ys.append(Y)
    Pairs.append([X, Y, V])

Xs.sort()
ore_count, value_sum, answer = 0, 0, 0

x_idx = len(Xs) - 1
x = Xs[x_idx]
y = 0

while (y <= max(Ys)) :

    if ore_count <= C:
        for pair in Pairs:
            px, py, pv = pair[0], pair[1], pair[2]
            if (px <= x and py <= y):
                ore_count += 1
                value_sum += pv
    else:
        x_idx -= 1
        ore_count -= 1
        value_sum -= 1
        print(" ")

    y += 1

print(Pairs)
print(Xs)