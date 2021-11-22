import sys
sys.stdin = open("input.txt", "r")

def electric_bus(K, N, M):
    # 일단 최대한 가보고 갔을 때 정류장이 없으면 뒤로 돌아가서 충전하는 방식으로 짜보자

    # 현재, 충전 횟수 초기화
    now, charged = 0, 0

    # 현재 위치가 N보다 작은 동안 반복한다.
    while now < N:
        # 일단 최대한 가본다.
        now += K
        # 최대한 갔을 때의 위치가 마침 충전소가 있으면 충전해주고 다음으로 넘어간다.
        if now in stations:
            charged += 1
            continue
        # 최대한 갔을 때가 충전소가 아닐 경우
        else:
            # 현재이미 목적지에 도착했을 경우 break
            if now >= N:
                break
            # 아무리 해도 도착을 못하는 경우가 있다.
            # 최대한 갔는데 충전소가 없고 가장 가까운 충전소가 이전에 충전한 곳이라면 도착을 못한다.
            prev_now = now - K
            for j in range(now, 0, -1):
                if charging_stations[j]:
                    now = j
                    charged += 1
                    # 가장 가까운 충전소가 이미 들렀던 곳이라면 도착할 수 없으니 return하자.
                    if now == prev_now:
                        return 0
                    break
    # 충전횟수를 return
    return charged

T = int(input())
for tc in range(1, T+1):
    # K = 한번의 충전으로 최대 이동 가능한 정류장 수
    # N = 목표지점
    # M = M개의 정류장 개수
    K, N, M = map(int, input().split())
    stations = list(map(int, input().split()))
    charging_stations = [0] * (N + 1)
    for i in range(M):
        charging_stations[stations[i]] = 1
    print("#{} {}".format(tc, electric_bus(K, N, M)))