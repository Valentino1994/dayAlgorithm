def solution(compressed):
    answer = ''

    stack = []

    for com in compressed:

        if com.isnumeric():
            stack.append(com)
            continue

        elif com == ")":
            nowStr = stack.pop()
            num = stack.pop()
            stack.append(nowStr*int(num))

        

    return answer