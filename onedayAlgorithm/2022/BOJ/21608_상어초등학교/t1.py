import sys
sys.stdin = open("input.txt")

N = int(input())
students = []

for _ in range(N**2):
    students.append(list(map(int, input().split(" "))))

class_room = [[0 for _ in range(N)] for _ in range(N)]

def check_wall(position):
    r, c = position
    if 0 <= r < N and 0 <= c < N:
        return True
    return False

def check_empty_chair():
    result = []
    for i in range(N):
        for j in range(N):
            if class_room[i][j] == 0:
                result.append([i, j])
    return result

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def check_like_student(empty_chairs, like_student):
    result = []
    for index, empty_chair in enumerate(empty_chairs):
        r, c = empty_chair
        temp = 0
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if check_wall((nr, nc)) and class_room[nr][nc] in like_student:
                temp += 1
        result.append([temp, index])

    return result

# 여기 왔다는 건 이미 두가지 이상의 chair를 갖는다는 것이다.
def check_empty_space(chairs_with_like_student, empty_chairs):

    next_chairs = [empty_chairs[chairs_with_like_student[0][1]]]
    max_like_students = chairs_with_like_student[0][0]
    for i in range(1, len(chairs_with_like_student)):
        if chairs_with_like_student[i][0] != max_like_students:
            break
        next_chairs.append(empty_chairs[chairs_with_like_student[i][1]])

    result = []
    for index, next_chair in enumerate(next_chairs):
        r, c = next_chair
        temp = 0
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if check_wall((nr, nc)) and class_room[nr][nc] == 0:
                temp += 1
        result.append([temp, index])

    return result, next_chairs

def check_row_column(chairs_with_space_number, next_chairs):

    result = [next_chairs[chairs_with_space_number[0][1]]]
    max_space = chairs_with_space_number[0][0]
    for i in range(1, len(chairs_with_space_number)):
        if chairs_with_space_number[i][0] != max_space:
            break
        result.append(next_chairs[chairs_with_space_number[i][1]])

    return result

def find_chair(now_student, like_student):
    # 현재 빈 의자들을 모두 구함
    empty_chairs = check_empty_chair()
    # 현재 빈 의자들을 보면서
    chairs_with_like_student = check_like_student(empty_chairs, like_student)
    chairs_with_like_student.sort(reverse=True)

    if len(chairs_with_like_student) == 1:
        r, c = empty_chairs[chairs_with_like_student[0][1]]
        class_room[r][c] = now_student
        return

    if chairs_with_like_student[0][0] > chairs_with_like_student[1][0]:
        r, c = empty_chairs[chairs_with_like_student[0][1]]
        class_room[r][c] = now_student
        return

    chairs_with_space_number, next_chairs = check_empty_space(chairs_with_like_student, empty_chairs)
    chairs_with_space_number.sort(reverse=True)
    if chairs_with_space_number[0][0] > chairs_with_space_number[1][0]:
        r, c = next_chairs[chairs_with_space_number[0][1]]
        class_room[r][c] = now_student
        return

    # 주변의 빈 공간 갯수가 같은 애들을 받아옴
    chairs_of_row_column = check_row_column(chairs_with_space_number, next_chairs)
    chairs_of_row_column.sort()
    if chairs_of_row_column[0][0] > chairs_of_row_column[1][0]:
        r, c = chairs_of_row_column[0]
        class_room[r][c] = now_student
        return
    else:
        chairs_sorted_by_column = [chairs_of_row_column[0]]
        for i in range(len(chairs_of_row_column)-1):
            if chairs_of_row_column[i][0] != chairs_of_row_column[i+1][0]:
                break
            chairs_of_row_column.append(chairs_of_row_column[i+1])
        chairs_sorted_by_column.sort()
        r, c = chairs_sorted_by_column[0]
        class_room[r][c] = now_student
        return

def calculate_answer(student_dict):
    result = 0
    for i in range(N):
        for j in range(N):
            now_student = class_room[i][j]
            now_like_students = student_dict[now_student]
            temp = 0
            for k in range(4):
                nr = i + dr[k]
                nc = j + dc[k]
                if check_wall((nr, nc)):
                    target = class_room[nr][nc]
                    if target in now_like_students:
                        if temp == 0:
                            temp += 1
                        else:
                            temp *= 10
            result += temp
    return result

def solution():
    student_dict = dict()
    for i in range(len(students)):
        now_student = students[i][0]
        like_student = students[i][1:5]

        student_dict[now_student] = like_student

        find_chair(now_student, like_student)

    return calculate_answer(student_dict)

print(solution())