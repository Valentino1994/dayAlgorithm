from collections import defaultdict
def solution(n, student, point):
    answer = 0

    half = int(n/2)
    good_student = []
    bad_student = []
    point_dict = dict()

    # 초기 세팅
    for i in range(n):
        point_dict[i+1] = 0

    for i in range(half):
        good_student.append(i+1)
    for i in range(half, n):
        bad_student.append(i+1)

    for i in range(len(student)):
        now_student = student[i]
        now_point = point[i]
        # 득점
        point_dict[now_student] += now_point
        # 현재 학생이 우반에 있다면 열반 아이들을 보면서 바뀌는지 본다.
        if now_student in good_student:
            should_change = False
            stdt = 0
            # 동점이라면 번호가 큰 아이가 열반으로 가기 때문에 뒤에서부터 본다.
            for j in range(len(good_student)-1, -1, -1):
                stdt = bad_student[j]
                # 열반에 있는 아이의 점수가 현재 점수와 같은데 현재 아이가 번호가 더 크다면 바꿔준다.
                if point_dict[now_student] == point_dict[stdt] and now_student > stdt:
                    should_change = True
                    break
                # 열반에 있는 아이의 점수가 더 크다면 바꾸는 애가 있다..
                elif point_dict[now_student] < point_dict[stdt]:
                    should_change = True
                    break

            if should_change:
                # 바꿀 때는 항상 min값을 바꿔준다.
                change_point = point_dict[stdt]
                for st in bad_student:
                    # 더 작은 애가 있으면 바꿔줌. 아니라면 이미 학생 번호 순서대로 봤기 때문에 안바꿔줌.
                    if point_dict[st] < change_point:
                        stdt = st
                        change_point = point_dict[st]

                answer += 1

                good_student.remove(now_student)
                bad_student.remove(stdt)
                good_student.append(stdt)
                bad_student.append(now_student)

                # 원본 정렬
                good_student.sort()
                bad_student.sort()

                continue

        # 현재 학생이 열반에 있다면 우반 아이들을 보면서 바뀌는지 본다.
        else:
            should_change = False
            stdt = 0
            # 동점이라면 번호가 큰 아이가 열반으로 가기 때문에 뒤에서부터 본다.
            for j in range(len(good_student)-1, -1, -1):
                stdt = good_student[j]
                # 우반에 있는 아이의 점수가 현재 점수와 같은데 현재 아이가 번호가 더 적다면 바꿔준다.
                if point_dict[now_student] == point_dict[stdt] and now_student < stdt:
                    should_change = True
                    break
                elif point_dict[now_student] > point_dict[stdt]:
                    should_change = True
                    break

            if should_change:
                answer += 1

                # 바꿀 때는 항상 min값을 바꿔준다.
                change_point = point_dict[stdt]
                for st in good_student:
                    # 더 작은 애가 있으면 바꿔줌. 아니라면 이미 학생 번호 순서대로 봤기 때문에 안바꿔줌.
                    if point_dict[st] < change_point:
                        stdt = st
                        change_point = point_dict[st]

                good_student.remove(stdt)
                bad_student.remove(now_student)
                good_student.append(now_student)
                bad_student.append(stdt)

                # 원본 정렬
                good_student.sort()
                bad_student.sort()

                continue

    return answer

n = 10
student = [3, 2, 10, 2, 8, 3, 9, 6, 1, 2]
point = [3, 2, 2, 5, 4, 1, 2, 1, 3, 3]

print(solution(n, student, point))