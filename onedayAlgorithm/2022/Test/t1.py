def solution(stack1, stack2, stack3):
    # write your code in Python 3.8.10
    answer = ""

    temp = []

    for num in stack1:
        temp.append([num, 1])

    for num in stack2:
        temp.append([num, 2])


    for num in stack3:
        temp.append([num, 3])

    result = sorted(temp)

    for i in range(len(result)-1, -1, -1):
        answer += str(result[i][1])

    return answer