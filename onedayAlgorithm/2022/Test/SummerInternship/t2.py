def solution(queue1, queue2):
    answer = 0
    purpose = int((sum(queue1) + sum(queue2)) / 2)
    # 무조건 안되는 경우 => (sum(q1) + sum(q2)) / 2 보다 큰 원소가 존재할 때
    for i in range(len(queue1)):
        if queue1[i] > purpose or queue2[i] > purpose:
            return -1

    # 입력이 300,000이라 재귀는 사용할 수 없음 brute force로 가자
    while sum(queue1) != purpose and sum(queue2) != purpose:

        if sum(queue1) > sum(queue2):
            value = queue1.pop(0)
            queue2.append(value)
        else:
            value = queue2.pop(0)
            queue1.append(value)
        answer += 1

    return answer

queue1 = [3, 2, 7, 2]
queue2 = [4, 6, 5, 1]

print(solution(queue1, queue2))