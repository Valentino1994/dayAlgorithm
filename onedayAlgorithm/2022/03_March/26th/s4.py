def solution(arr, brr):
    answer = -1
    for i in range(len(arr)):
        # 현재 볼 셀이 원하는 셀보다 크거나 같으면 볼 필요가 없다.
        if arr[i] >= brr[i]:
            continue

        # 시작 셀이라면
        if i == 0:
            # 시작 셀의 오른쪽 셀이 원하는 너비보다 크면 거기서 빼올 수 있다.
            if arr[i + 1] > brr[i + 1]:
                answer += 1
                # 단 가져올 수 있는 max는 이렇게 된다.
                max_num = arr[i + 1] - brr[i + 1]
                while max_num != 0:
                    arr[i] += 1
                    arr[i + 1] -= 1
                    max_num -= 1
                    if arr[i] == brr[i]:
                        break

        # 마지막 셀이라면
        elif i == len(arr):
            if arr[i - 1] > brr[i - 1]:
                # 단 가져올 수 있는 max는 이렇게 된다.
                max_num = arr[i - 1] - brr[i - 1]
                while max_num != 0:
                    arr[i] += 1
                    arr[i - 1] -= 1
                    max_num -= 1
                    if arr[i] == brr[i]:
                        break

        # 양 끝이 아니라면 둘 다 본다.
        else:

            if arr[i - 1] > brr[i - 1]:
                answer += 1
                # 단 가져올 수 있는 max는 이렇게 된다.
                max_num = arr[i - 1] - brr[i - 1]
                while max_num != 0:
                    arr[i] += 1
                    arr[i - 1] -= 1
                    max_num -= 1
                    if arr[i] == brr[i]:
                        break

            if arr[i + 1] > brr[i + 1]:
                answer += 1
                # 단 가져올 수 있는 max는 이렇게 된다.
                max_num = arr[i + 1] - brr[i + 1]
                while max_num != 0:
                    arr[i] += 1
                    arr[i + 1] -= 1
                    max_num -= 1
                    if arr[i] == brr[i]:
                        break

    return answer + 1

# 코드가 많이 겹치니까 시간 남으면 리팩토링해야겠다.