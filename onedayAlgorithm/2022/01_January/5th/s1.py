def solution(N, Arr):

    answer = 0

    arr = sorted(Arr)[::-1]
    idx = 1
    max_num = sum(Arr)

    while idx < max_num:
        tmp = idx
        for coin in arr:
            tmp -= coin
            if tmp == 0:
                break
            elif tmp < 0:
                tmp += coin
        if tmp != 0:
            answer = idx
            break
        else:
            idx += 1

    return answer

N = 3
Arr = [3, 5, 7]

print(solution(N, Arr))