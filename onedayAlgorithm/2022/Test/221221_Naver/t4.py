def solution(A):
    # Implement your solution here
    answer = 0
    start = 987654321
    end = 0
    alternative_list = []
    for i in range(len(A)-2):
        how_many_success = check_alternative(i)

        if how_many_success == 2:
            start = min(start, i)
            end = i + how_many_success
        else:
            alternative_list.append((start, end))
            start = i + how_many_success + 1

    answer = get_answer(start, end)
    alternative_list.append((start, end))
    return get_answer(start, end)

def check_alternative(now):
    result = 0
    # 다음 것 성공
    if should_different(A[now], A[now + 1]):
        result += 1
    else:
        return result

    if should_same(A[now], A[now + 2]):
        result += 1
    else:
        return result

    return result

def should_different(now, before):
    result = 0

    # 둘 중 하나가 0이면 무조건 맞음
    if now == 0 or before == 0:
        result = 1
    elif now > 0 and before < 0:
        result = 1
    elif now < 0 and before > 0:
        result = 1

    return result

def should_same(now, before):
    result = False

    # 둘 중 하나가 0이면 무조건 맞음
    if now == 0 or before == 0:
        result = True
    elif now > 0 and before > 0:
        result = True
    elif now < 0 and before < 0:
        result = True

    return result

def get_answer(start, end):
    # start와 end가 같다는 것은 모두 alternate 하다는 것
    if start == end:
        return len(A)
    # 이 외에는 모두 빼줌
    else:
        return end - start

A = [1, 2, 3]
print(solution(A))
A1 = [0, 0, 0]
print(solution(A1))