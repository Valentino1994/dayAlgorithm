def solution(N, Arr):
    answer = 0

    arr = sorted(Arr)[::-1]
    idx = 0

    while idx < N:
        idx += arr[idx]
        answer += 1
        
    return answer

N = 5
Arr = [2, 3, 1, 2, 2]

print(solution(N, Arr))