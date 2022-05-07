def solution(rc, operations):
    answer = []

    for operation in operations:
        if operation == "Rotate":
            rc = rotate(rc)
        else:
            rc = shiftRow(rc)

    answer = rc

    return answer

def shiftRow(rc):
    new = []
    new.append(rc[len(rc) - 1])
    # 1번째 인덱스부터 넣고 마지막에 0번 인덱스를 추가하면 shiftRow
    for i in range(0, len(rc) - 1):
        new.append(rc[i])

    return new

def rotate(rc):
    new_rc = rc[:]

    rowend_index = len(rc) - 1
    colend_index = len(rc[0]) - 1
    # 바깥쪽만 한바퀴 돌림

    new = []
    new.append([rc[1][0]] + rc[0][:colend_index])
    end = rc[rowend_index][1:colend_index + 1] + [rc[rowend_index - 1][colend_index]]
    # 그 다음 좌우를 바꿔줘야함
    # 먼저 왼쪽은 아래에서 위로 올림
    temp_left = []
    for i in range(1, rowend_index + 1):
        temp_left.append(rc[i][0])
    temp_left.append(rc[rowend_index][1])
    # 다음 오른쪽은 위에서
    temp_right = []
    temp_right.append(rc[0][colend_index - 1])
    for i in range(0, rowend_index):
        temp_right.append(rc[i][colend_index])

    for i in range(len(temp_left)):
        new_rc[i][0] = temp_left[i]
        new_rc[i][colend_index] = temp_right[i]

    for i in range(1, rowend_index):
        new.append(new_rc[i])

    new.append(end)

    return new