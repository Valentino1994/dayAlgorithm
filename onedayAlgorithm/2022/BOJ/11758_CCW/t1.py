import sys
sys.stdin = open("input.txt")

points = []
for _ in range(3):
    points.append(list(map(int, input().split(" "))))

def calculate_slope(before_point, next_point):
    x1, y1 = before_point
    x2, y2 = next_point

    if y2 - y1 == 0 or x2 - x1 == 0:
        return 0

    return int((y2 - y1) / (x2 - x1))

def check_direction(before_point, next_point):
    x1, y1 = before_point
    x2, y2 = next_point
    # 방향이 1사분면, 2사분면, 3사분면, 4사분면 인지
    if x2 - x1 > 0 and y2 - y1 > 0:
        return 1
    elif x2 - x1 < 0 and y2 - y1 > 0:
        return 2
    elif x2 - x1 < 0 and y2 - y1 < 0:
        return 3
    elif x2 - x1 > 0 and y2 - y1 < 0:
        return 4

def check_clockwise(points):
    first_direction = check_direction(points[0], points[1])
    second_direction = check_direction(points[1], points[2])
    if first_direction == 1 or first_direction == 3:
        if second_direction == 1 or second_direction == 2:
            return 1
        else:
            return -1
    elif first_direction == 2:
        if second_direction == 1 or second_direction == 4:
            return 1
        else:
            return -1
    elif first_direction == 4:
        if second_direction == 2 or second_direction == 3:
            return 1
        else:
            return -1

def check_answer(first_slope, second_slope):
    if first_slope == second_slope:
        return 0
    else:
        return check_clockwise(points)

first_slope = calculate_slope(points[0], points[1])
second_slope = calculate_slope(points[1], points[2])

print(check_answer(first_slope, second_slope))