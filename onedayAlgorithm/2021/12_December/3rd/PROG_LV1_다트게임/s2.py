# 이번에 맞춘 코드

def solution(dartResult):
    answer = 0
    stack = []
    now_number = 0
    for i in range(len(dartResult)):
        # 만약 숫자라면
        if dartResult[i].isnumeric():
            if dartResult[i] == "1" and i < len(dartResult) and dartResult[i+1] == "0":
                now_number = 10
            elif dartResult[i] == "0" and i > 0 and dartResult[i - 1] == "1":
                continue
            else:
                now_number = int(dartResult[i])
        # 만약 알파벳이라면 ?
        elif dartResult[i].isalpha():
            if dartResult[i] == "S":
                stack[len(stack) - 1] = stack[len(stack) - 1] ** 1
                continue
            elif dartResult[i] == "D":
                stack[len(stack) - 1] = stack[len(stack) - 1] ** 2
                continue
            else:
                stack[len(stack) - 1] = stack[len(stack) - 1] ** 3
                continue
        # 알파벳도 아니고 숫자도 아니라면 ?
        elif not dartResult[i].isalnum():
            if dartResult[i] == "*":
                stack[len(stack) - 1] = stack[len(stack) - 1] * 2
                # 이전 점수가 있다면 이전 점수도 2배를 해줘야한다.
                if len(stack) > 1:
                    stack[len(stack) - 2] = stack[len(stack) - 2] * 2
                continue
            else:
                stack[len(stack) - 1] = stack[len(stack) - 1] * -1
                continue
        stack.append(now_number)

    answer = sum(stack)

    return answer

dartResult = "10D4S10D"
print(solution(dartResult))