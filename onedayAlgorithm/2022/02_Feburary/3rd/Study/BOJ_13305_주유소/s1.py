import sys
sys.stdin = open("input.txt", "r")

N = int(input())
distances = list(map(int, input().split()))
cities = list(map(int, input().split()))

city_distance = []
for i in range(N-1):
    oil_price = []
    tmp = 0
    for j in range(i, N-1):
        tmp += distances[j] * cities[i]
        oil_price.append(tmp)
    city_distance.append(oil_price)

result = 987654321
city_idx = 1
value = 0

def city_permutation(value, city_idx):
    global result
    if city_idx == N:
        if value < result:
            result = value
        return

    now_city = city_distance[city_idx - 1]

    for i in range(1, len(now_city)+1):
        city_permutation(value + now_city[i-1], city_idx + i)

city_permutation(value, city_idx)
print(result)
