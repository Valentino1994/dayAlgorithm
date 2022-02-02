import sys
sys.stdin = open("input.txt", "r")

#input = sys.stdin.readline

N = int(input())
distances = list(map(int, input().split()))
cities = list(map(int, input().split()))

result = distances[0] * cities[0]
minimum_price = cities[0]
city_distance = 0

for i in range(1, N-1):
    if cities[i] < minimum_price:
        result += minimum_price * city_distance
        city_distance = distances[i]
        minimum_price = cities[i]
    else:
        city_distance += distances[i]

    if i == N-2:
        result += minimum_price * city_distance

print(result)
