def solution(people, limit):
    answer = 0

    people = sorted(people)
    people_count = len(people)

    visited = [0] * people_count

    for i in range(people_count):

        if visited[i] != 0:
            continue

        if i == people_count-1:
            answer += 1
            break

        now = people[i]
        temp_next = people[i+1]
        visited[i] = 1

        for j in range(i + 1, people_count):

            if visited[j] == 0 and now + people[j] < limit:
                temp_next = people[j]

            elif now + people[j] == limit:
                visited[j] = 1
                answer += 1
                break

            else:
                visited[j-1] = 1
                answer += 1
                break

    return answer

people = [70, 50, 80, 50]
limit = 100

print(solution(people, limit))