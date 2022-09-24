from typing import List
import math

def solution(queries: List[List[int]]) -> int:
    answer = 0

    everyArray = [[0, 0] for _ in range(1001)]
    for query in queries:
        arrayIndex = query[0]
        arrayItems = query[1]

        sumItems = everyArray[arrayIndex][1] + arrayItems

        if everyArray[arrayIndex][0] == 0:
            everyArray[arrayIndex][0] = howManyTwo(arrayItems)
            everyArray[arrayIndex][1] = arrayItems
            continue

        sizeOfbuffer = int(math.pow(2, everyArray[arrayIndex][0]))
        if sumItems > sizeOfbuffer:
            answer += everyArray[arrayIndex][1]
            everyArray[arrayIndex][0] = howManyTwo(arrayItems)
            everyArray[arrayIndex][1] += arrayItems

        else:
            everyArray[arrayIndex][1] += arrayItems

    return answer

def howManyTwo(number: int) -> int:

    result = 1

    while number > 2:
        result += 1
        number /= 2

    return result

queries = [[2, 10], [7, 1], [2, 5], [2, 9], [7, 32]]
print(solution(queries))