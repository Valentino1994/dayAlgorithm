def solution(S):
    answer = 0

    for s in S:
        if s == '0':
            continue
        if answer == 0:
            answer = int(s)
            continue
        answer *= int(s)

    return answer

S = '567'

print(solution(S))