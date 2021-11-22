import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for t in range(1, T+1):
    N = int(input())
    Array = list(map(int, input().split()))
    # 가장 큰 수와 가장 작은 수를 구한다.
    max_num = 0
    min_num = 1000000
    # 한번의 반복문으로 가능하다.
    for i in range(N):
        if Array[i] > max_num:
            max_num = Array[i]
        if Array[i] < min_num:
            min_num = Array[i]
    print("#{0} {1}".format(t, (max_num - min_num)))