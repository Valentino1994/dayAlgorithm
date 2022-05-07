def solution(survey, choices):
    answer = ''
    # 점수를 파악하기 위한 것
    scores = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}

    # 1~7 매우 비동의 ~ 매우 동의
    # 왼쪽은 비동의에 점수 오른쪽은 동의에 점수
    for i, choice in enumerate(choices):
        # 모르겠으면 아무 변화가 없음으로 먼저 넘어감
        if choice == 4:
            continue
        # 비동의일 때
        if choice < 4:
            character = survey[i][0]
            # 매우 비동의 == 1 | 비동의 == 2 | 약간 비동의 == 3 임으로 4를 뺀 절대값이 점수임
            scores[character] += abs(choice - 4)

        else:
            character = survey[i][1]
            # 매우 동의 == 7 | 동의 == 6 | 약간 동의 == 5 임으로 4를 뺀 값이 점수임
            scores[character] += choice - 4

    temp = []
    for k, v in scores.items():
        temp.append([k, v])

    for i in range(0, len(temp) - 1, 2):
        if temp[i][1] == temp[i + 1][1] or temp[i][1] > temp[i + 1][1]:
            answer += temp[i][0]

        else:
            answer += temp[i + 1][0]

    return answer

survey = ["AN", "CF", "MJ", "RT", "NA"]
choices = [5, 3, 2, 7, 5]

print(solution(survey, choices))

