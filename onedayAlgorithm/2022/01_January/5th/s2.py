from itertools import combinations


def solution(Arr):

    answer = 0

    for c in combinations(Arr, 2):
        if c[0] != c[1]:
            answer += 1

    return answer

Arr = [1, 5, 4, 3, 2, 4, 5, 2]

print(solution(Arr))