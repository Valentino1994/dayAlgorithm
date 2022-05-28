import math

def solution(fuel, powers, distances):
    answer = 0
    temp = []

    # If there is only fuels can provide 1 for every spaceship
    if fuel == len(powers):
        for i in range(len(powers)):
            temp.append(calcSec(1, powers[i], distances[i]))
        answer = max(temp)
        return answer

    # power와 distance의 가중치를 계산해서 비율을 메긴다.
    # 비율을 메겼을 때 전체 정수의 합이 fuel 보다 크면 어떡하지...?
    temp_arr = []
    for i in range(len(distances)):
        temp_arr.append(math.ceil(distances[i]/powers[i]))

    make(fuel, temp_arr)

    return temp_arr

def calcSec(f, p, d):
    answer = f
    speed = f*p
    d -= f*speed // 2
    answer += math.ceil(d / speed)
    return answer

def make(N, arr):
    result = []

    for item in arr:
        result.append(item/N)

    return result

fuel = 4
powers = [40, 30, 20, 10]
distances = [1000, 2000, 3000, 4000]

solution(fuel, powers, distances)