import sys
sys.stdin = open("input.txt", "r")

# N == Node | M == edge | K == 이만큼 떨어진 도시 | X == 시작 도시 번호
N, M, K, X = map(int, input().split())
# edge의 정보를 받아온다.
infos = [list(map(int, input().split())) for _ in range(M)]
# 빈 node를 만다.
cities = [[] for _ in range(N+1)]

for info in infos:
    r, c = info[0], info[1]
    cities[r].append(c)

# 먼저 거리가 1인 것들을 담아둔다.
stack = cities[X][:]
visited = [0] * (N + 1)
result = 0

def find_city(cnt):

    global result

    if cnt == K:
        result += 1
        return

    if cnt > K:
        return

    while stack:
        city_num = stack.pop(0)
        visited[city_num] = 1
        cnt += 1

        for city in cities[city_num]:
            if visited[city] == 0:
                stack.append(city)
                find_city(cnt)

print(cities[X])
print(infos)
print(cities)
find_city(0)
print(result)