def solution(cap, n, deliveries, pickups):
    answer = 0

    deliveries.insert(0, -1)
    pickups.insert(0, -1)

    while True:
        endDistance = findEnd(cap, n, deliveries, pickups)

        # 끝까지 왔으면 종료
        if endDistance == 0:
            break

        nowTruck = cap

        for i in range(endDistance, 0, -1):

            if nowTruck - deliveries[i] >= 0:
                nowTruck -= deliveries[i]
                deliveries[i] = 0
            else:
                deliveries[i] -= (cap - nowTruck)
                break

            if nowTruck + pickups[i] < cap:
                nowTruck += pickups[i]
                pickups[i] = 0
            elif nowTruck + pickups[i] == cap:
                pickups[i] = 0
                if nowTruck:
                    continue
                else:
                    break
            else:
                pickups[i] -= cap
                break

        answer += (endDistance * 2)

    return answer

def findEnd(cap, n, deliveries, pickups) -> int:

    endDistance = 0

    for i in range(n, 0, -1):
        if deliveries[i] != 0:
            endDistance = max(endDistance, i)
            break

        if pickups[i] != 0:
            endDistance = max(endDistance, i)
            break

    return endDistance

cap = 4
n = 5
deliveries = [1, 0, 3, 1, 2]
pickups = [0, 3, 0, 4, 0]
cap1 = 2
n1 = 7
deliveries1 = [1, 0, 2, 0, 1, 0, 2]
pickups1 = [0, 2, 0, 1, 0, 2, 0]

print(solution(cap, n, deliveries, pickups))
print(solution(cap1, n1, deliveries1, pickups1))