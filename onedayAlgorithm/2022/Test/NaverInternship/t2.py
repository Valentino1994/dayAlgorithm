import math

def solution(M, N):
    result = 0

    # N이 없을 경우 M으로 만들 수 있는 가장 큰 정사각형은 제곱근의 버림이다.
    if N == 0:
        return int(math.sqrt(M))

    # M이 없을 경우 N으로 만들 수 있는 가장 큰 정사각형은 제곱근의 버림 * 타일의 크기이다.
    if M == 0:
        return int(math.sqrt(N)) * 2

    # 현재 만든 N으로 만든 제곱근에서 M을 만들면 다음 제곱근으로 갈 수 있는지 체크
    # 현재 N으로 만들 수 있는 정사각형의 한 변의 N의 개수
    now = int(math.sqrt(N))
    # 현재 N을 만들고 남은 N
    leftedN = N - now
    # 다음 정사각형의 한 변의 N의 개수
    next = now + 1
    # 다음으로 필요한 N의 개수
    need_N = (next * next) - (now * now) - leftedN

    # M으로 만들 수 있는 N의 개수
    NfromM = M // 4

    # N을 만들고 남는 M의 개수
    leftedM = M % 4

    # M으로 N의 제곱을 더 이상 못만든다면 N으로 만든 현재의 제곱근이 가장 큰 정사각형이다.
    if need_N > NfromM:
        return now * 2

    # M으로 다음 N의 제곱을 만들고 M이 남았다면 남은 M으로 다음 N의 제곱도 만들 수 있는지 체크한다.
    while NfromM >= need_N:
        NfromM -= need_N
        # 다음 제곱근을 만들고 남은 M은 다시 남은 M에 더해준다.
        leftedM += NfromM * 4
        # 현재 제곱근과 다음 제곱근에 1씩 더해준다.
        now += 1
        next += 1
        # 계속해서 반복한다.
        need_N = (next * next) - (now * now)
        NfromM = leftedM // 4
        leftedM = leftedM % 4

    # 위의 반복문이 끝나면 N과 M으로 만들 수 있는 최대의 정사각형을 만들 수 있다.
    # 그 후 현재 남은 M의 개수가 현재 최대 정사각형의 한 변의 길이 * 2 + 1이라면 남은 M으로 한번 둘러쌀 수 있다.
    # 그렇지 못하다면 현재의 정사각형
    if (now * 2) * 2 + 1 < M:
        return now * 2 + 1
    else:
        return now * 2

M = 13
N = 3

print(solution(M, N))