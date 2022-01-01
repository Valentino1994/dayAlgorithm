def solution(N, M, K, Arr):

    #1
    answer = 0
    arr = sorted(Arr)[::-1]
    cnt = K

    while M:
        M -= 1
        if cnt == 0:
            idx = 1
            cnt = K
        else:
            idx = 0
            cnt -= 1
        answer += arr[idx]

    return answer

N, M, K = 5, 7, 2
Arr = [3, 4, 3, 4, 3]

print(solution(N, M, K, Arr))