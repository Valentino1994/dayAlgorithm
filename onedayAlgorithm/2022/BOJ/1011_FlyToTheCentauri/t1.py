import sys
sys.stdin = open("input.txt")

tc = int(input())

def find_way(x, y):

    distance = y - x
    count = 0  # 이동 횟수
    move = 1  # count별 이동 가능한 거리
    move_plus = 0  # 이동한 거리의 합
    while move_plus < distance:
        count += 1
        move_plus += move  # count 수에 해당하는 move를 더함
        if count % 2 == 0:  # count가 2의 배수일 때,
            move += 1

    return count

def solution():
    x, y = list(map(int, input().split(" ")))
    return find_way(x, y)

for _ in range(tc):
    print(solution())