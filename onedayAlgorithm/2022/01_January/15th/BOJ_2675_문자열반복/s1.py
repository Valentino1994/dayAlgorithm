import sys
# input = sys.stdin.readline()
sys.stdin = open("input.txt", "r")

T = int(input())
for _ in range(T):

    N, words = input().split()
    result = ""

    for word in words:
        n = word * int(N)
        result += n

    print(result)