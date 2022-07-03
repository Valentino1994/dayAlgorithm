def solution(grade):
    answer = 0

    # 반복문을 뒤에서부터 돌면서 현재 인덱스의 값이 다음 인덱스의 값보다 작으면
    # 다음 인덱스의 값에서 현재 인덱스의 값을 뺀만큼 answer에 넣어주고,
    # 다음 인덱스의 값을 현재 인덱스의 값으로 바꿔준다.

    for i in range(len(grade)-1, 0, -1):
        if grade[i-1] > grade[i]:
            answer += (grade[i-1] - grade[i])
            grade[i-1] = grade[i]

    return answer

grade = [2, 1, 3]

print(solution(grade))