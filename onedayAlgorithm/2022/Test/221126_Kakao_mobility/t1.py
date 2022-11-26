def solution(flowers):
    answer = 0
    days = [0 for _ in range(366)]
    for flower in flowers:
        s, e = flower
        for i in range(s, e):
            days[i] += 1

    for day in days:
        if day != 0:
            answer += 1

    return answer

flowers = [[2, 5], [3, 7], [10, 11]]
print(solution(flowers))