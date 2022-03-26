def solution(abilities, k):
    answer = 0

    # 우선권을 써야하는 경우는 1순위와 2순위의 능력치가 가장 차이가 많이 날 때다.
    if len(abilities) % 2 != 0:
        abilities.append(0)

    n_abilities = sorted(abilities)[::-1]
    differences = []
    for i in range(0, len(abilities) - 1, 2):
        differences.append([n_abilities[i] - n_abilities[i + 1], i])

    differences.sort()
    # k를 써야하는 index는 그럼으로 아래와 같이 구할 수 있다.
    k_orders = []
    for i in range(len(differences) - 1, -1, -1):
        if k != 0:
            k_orders.append(differences[i][1])
            k -= 1

        else:
            break

    # 이제 index를 돌면서 현재 index가 우선권을 써야하는 상황이면 현재 index를 가져가고,
    # 아닐 경우에는 index + 1을 가져간다.
    for i in range(0, len(n_abilities) - 1, 2):
        if i in k_orders:
            answer += n_abilities[i]
        else:
            answer += n_abilities[i + 1]

    return answer