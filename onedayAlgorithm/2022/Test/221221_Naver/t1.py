def solution(A):
    # Implement your solution here
    bulb_sockets = [0 for _ in range(len(A))]

    answer = 0
    for bulb_index in A:
        now_index = bulb_index - 1
        bulb_sockets[now_index] = 1
        if check_turn_on_every_bulbs(bulb_sockets, now_index):
            answer += 1

    return answer

def check_turn_on_every_bulbs(bulb_sockets, now_bulb_index):
    for i in range(0, now_bulb_index):
        now_bulb = bulb_sockets[i]
        if now_bulb == 0:
            return False
    return True

A = [1, 3, 4, 2, 5]

print(solution(A))