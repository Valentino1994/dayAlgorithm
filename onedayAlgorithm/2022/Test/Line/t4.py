from typing import List
from collections import deque

def solution(wall: List[str]) -> List[List[int]]:
    wallSizeR = len(wall)
    wallSizeC = len(wall[0])
    holds = deque([[wallSizeR-1, 0]])

    answer = [[987654321] * wallSizeC for _ in range(wallSizeR)]
    answer[wallSizeR-1][0] = 1

    while holds:
        nowNode = holds.popleft()
        nowRoute = answer[nowNode[0]][nowNode[1]]
        everyHolds = findHold(wall, wallSizeR, wallSizeC, nowNode, answer)
        for hold in everyHolds:
            if goCheck(wall, wallSizeR, wallSizeC, hold, nowNode):
                holds.append([nowNode[0] + hold[0][0], nowNode[1] + hold[0][1]])
                if answer[nowNode[0] + hold[0][0]][nowNode[1] + hold[0][1]] > nowRoute + 1:
                    answer[nowNode[0] + hold[0][0]][nowNode[1] + hold[0][1]] = nowRoute + 1

    for i in range(wallSizeR):
        for j in range(wallSizeC):
            if answer[i][j] == 987654321:
                if wall[i][j] == "H":
                    answer[i][j] = -1
                else:
                    answer[i][j] = 0

    return answer

def findHold(wall: List[str], wallSizeR: int, wallSizeC: int, nowPosition: List[int], answer):

    holdPosition = []
    # hold로 넘어갈 수 있는 경우의 수는 총 8가지 앞의 3개는 무조건 넘어갈 수 있음
    # hold가 있을 경우 check 해야하는 경우의 수를 같이 넘겨줄 예정
    # 0 -> 무조건 이동 가능 | 1 -> 왼쪽으로 2칸 | 2 -> 오른쪽으로 2칸 | 3 -> 왼쪽 대각선 | 4 -> 오른쪽 대각선 | 5 -> 위로 2칸 | 6 -> 왼쪽으로 3칸 | 7 -> 오른쪽으로 3칸 | 8 -> 아래로 한칸
    cases = [(0, -1), (0, 1), (-1, 0), (0, -2), (0, 2), (-1, -1), (-1, 1), (-2, 0), (0, -3), (0, 3), (1, 0)]

    for i in range(0, len(cases)):

        newR = nowPosition[0] + cases[i][0]
        newC = nowPosition[1] + cases[i][1]
        # 벽체크 후 hold가 있다면 case와 함께 넣어줌
        if 0 <= newR < wallSizeR and 0 <= newC < wallSizeC and wall[newR][newC] == "H" and answer[newR][newC] == 987654321:
            checkPoint = i - 2
            if checkPoint < 1:
                checkPoint = 0
            holdPosition.append([cases[i], checkPoint])

    return holdPosition

def goCheck(wall: List[str], wallSizeR: int, wallSizeC: int, nowCase, nowNode) -> bool:

    result = False

    if nowCase[1] == 0:
        result = True

    # 왼쪽으로 2칸
    elif nowCase[1] == 1:
        wallPoints = [(0, -1), (-1, 0), (-1, -1), (-1, -2)]

        for wallPoint in wallPoints:
            newR = nowNode[0] + wallPoint[0]
            newC = nowNode[1] + wallPoint[1]
            if 0 <= newR < wallSizeR and 0 <= newC < wallSizeC and wall[newR][newC] == ".":
                pass
            else:
                return False

        result = True

    # 오른쪽으로 2칸
    elif nowCase[1] == 2:
        wallPoints = [(0, 1), (-1, 0), (-1, 1), (-1, 2)]

        for wallPoint in wallPoints:
            newR = nowNode[0] + wallPoint[0]
            newC = nowNode[1] + wallPoint[1]
            if 0 <= newR < wallSizeR and 0 <= newC < wallSizeC and wall[newR][newC] == ".":
                pass
            else:
                return False

        result = True
    # 왼쪽 대각선
    elif nowCase[1] == 3:
        wallPoints = [(-1, 0), (0, -1)]

        for wallPoint in wallPoints:
            newR = nowNode[0] + wallPoint[0]
            newC = nowNode[1] + wallPoint[1]
            if 0 <= newR < wallSizeR and 0 <= newC < wallSizeC and wall[newR][newC] == ".":
                pass
            else:
                return False

        result = True

    # 오른쪽 대각선
    elif nowCase[1] == 4:
        wallPoints = [(-1, 0), (0, 1)]

        for wallPoint in wallPoints:
            newR = nowNode[0] + wallPoint[0]
            newC = nowNode[1] + wallPoint[1]
            if 0 <= newR < wallSizeR and 0 <= newC < wallSizeC and wall[newR][newC] == ".":
                pass
            else:
                return False

        result = True

    # 위로 2칸
    elif nowCase[1] == 5:
        wallPoints = [(-1, 0)]

        for wallPoint in wallPoints:
            newR = nowNode[0] + wallPoint[0]
            newC = nowNode[1] + wallPoint[1]
            if 0 <= newR < wallSizeR and 0 <= newC < wallSizeC and wall[newR][newC] == ".":
                pass
            else:
                return False

        result = True

    # 왼쪽으로 3칸
    elif nowCase[1] == 6:
        wallPoints = [(0, -1), (0, -2), (-1, 0), (-1, -1), (-1, -2), (-1, -3)]

        for wallPoint in wallPoints:
            newR = nowNode[0] + wallPoint[0]
            newC = nowNode[1] + wallPoint[1]
            if 0 <= newR < wallSizeR and 0 <= newC < wallSizeC and wall[newR][newC] == ".":
                pass
            else:
                return False

        result = True

    # 오른쪽으로 3칸
    elif nowCase[1] == 7:
        wallPoints = [(0, 1), (0, 2), (-1, 0), (-1, 1), (-1, 2), (-1, 3)]

        for wallPoint in wallPoints:
            newR = nowNode[0] + wallPoint[0]
            newC = nowNode[1] + wallPoint[1]
            if 0 <= newR < wallSizeR and 0 <= newC < wallSizeC and wall[newR][newC] == ".":
                pass
            else:
                return False

        result = True

    elif nowCase[1] == 8:
        result = True

    return result

wall = ["H.H", ".HX", "H.H"]
wall2 = ["....HH", "H..H.H"]
print(solution(wall))
print(solution(wall2))