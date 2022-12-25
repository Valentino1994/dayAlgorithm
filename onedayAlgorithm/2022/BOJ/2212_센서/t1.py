import sys
sys.stdin = open("input.txt")

def solution():
    n = int(input())
    k = int(input())
    loads = list(map(int, input().split(" ")))

    if k >= n:
        return 0

    loads = sorted(loads)

    distances = []
    for i in range(1, n):
        distances.append(loads[i] - loads[i - 1])

    distances = sorted(distances, reverse=True)

    for _ in range(k - 1):
        distances.pop(0)

    return sum(distances)

print(solution())