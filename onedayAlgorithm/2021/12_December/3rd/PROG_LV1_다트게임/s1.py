# 이전에 실패한 코드

def solution(dartResult):
    answer = 0
    result = []
    stack = []

    for i in range(-1, -(len(dartResult) + 1), -1):
        tmp = []
        if dartResult[i].isnumeric():
            stack.append(dartResult[i])
            while stack:
                tmp += [stack.pop()]
            result.append(tmp)
        else:
            stack.append(dartResult[i])
    new_result = sorted(result)
    tmp_list = []
    for i in range(len(new_result)):
        tmp = 0
        for j in range(len(new_result[i])):

            if new_result[i][j].isnumeric():
                tmp += int(new_result[i][j])

            else:
                if new_result[i][j] == 'S':
                    tmp = tmp ** 1

                elif new_result[i][j] == 'D':
                    tmp = tmp ** 2

                elif new_result[i][j] == 'T':
                    tmp = tmp ** 3

                elif new_result[i][j] == '#':
                    tmp = tmp * (-1)

                elif new_result[i][j] == '*':
                    tmp = tmp * 2
                    try:
                        tmp_list[-1] = tmp_list[-1] * 2
                    except:
                        pass
        tmp_list += [tmp]
    for i in tmp_list:
        answer += i
    return answer