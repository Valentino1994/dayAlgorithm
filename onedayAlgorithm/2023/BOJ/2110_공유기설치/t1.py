import sys
sys.stdin = open("input.txt")

N, C = list(map(int, input().split(" ")))
homes = []
for _ in range(N):
    homes.append(int(input()))

homes.sort()

count = 2
distance = homes[-1] - homes[0]
points = [0, N-1]

while count != C:

    distance_list = []

    for i in range(len(points)-1):
        left_point = points[i]
        right_point = points[i + 1]

        for this_point in range(left_point+1, right_point):
            now_distances = [abs(homes[left_point] - homes[this_point]), abs(homes[right_point] - homes[this_point])]
            distance_list.append([this_point, now_distances])

    maximum_distance = 0
    maximum_point = 0
    for d in distance_list:
        if min(d[1]) > maximum_distance:
            maximum_distance = min(d[1])
            maximum_point = d[0]

    distance = maximum_distance
    points.append(maximum_point)
    points.sort()

    count += 1

print(distance)