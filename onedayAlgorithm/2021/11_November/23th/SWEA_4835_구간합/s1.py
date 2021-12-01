import sys
sys.stdin = open("input.txt", "r")

def SectionSum(N, M):
    # 합이 가장 클 수 있는 것은 N <= 10000, a <= 100 임으로 이렇게 초기화 함
    min_sum = (10000 * 100)
    max_sum = 0
    # range는 넣은 숫자 바로 앞의 수까지 본다는 것에 주의
    for i in range(N-M+1):
        tmp = 0
        for j in range(i, i+M):
            tmp += numbers[j]
        # tmp값을 현재 최소값과 최대값과 비교
        if tmp > max_sum:
            max_sum = tmp
        if tmp < min_sum:
            min_sum = tmp
    # 반환해야하는 것은 최대값과 최소값의 차이
    return max_sum - min_sum

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    numbers = list(map(int, input().split()))
    print("#{} {}".format(tc, SectionSum(N, M)))