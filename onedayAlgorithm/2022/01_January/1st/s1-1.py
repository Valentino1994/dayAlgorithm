def solution(N, M, K, Arr):

    arr = sorted(Arr)[::-1]
    first = arr[0]
    second = arr[1]

    answer = 0

    count = M // (K + 1)
    count += M % (K + 1)

    answer += (count * K * first)
    answer += (count * second)

    return answer

N, M, K = 5, 8, 3
Arr = [2, 4, 5, 4, 6]

print(solution(N, M, K, Arr))