def solution(S):
    answer = -1

    start = S[0]

    for s in S:
        if s != start:
            answer += 1
            start = s

    return answer

S = '0001100'

print(solution(S))