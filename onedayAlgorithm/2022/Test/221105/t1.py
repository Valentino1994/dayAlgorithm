def solution(line):

    answer = ''
    now = line[0]
    flag = False
    for i in range(1, len(line)):
        # 같으면 그냥 넘어간다.
        # 같은게 있다고 체크한 후 answer에 넣지 않고 넘어간다.
        if line[i] == now:
            flag = True
            continue

        # 다르면 answer에 now를 추가
        else:
            answer += now
            now = line[i]
            if flag:
                answer += "*"
                flag = False

    if flag:
        answer += now
        answer += "*"
    else:
        answer += now

    return answer

line = "aabbbc"
print(solution(line))