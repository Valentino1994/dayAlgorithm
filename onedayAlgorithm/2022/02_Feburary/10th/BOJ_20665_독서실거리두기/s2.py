import sys
sys.stdin = open("input.txt", "r")
from collections import defaultdict

def enter(e, seats, seat):
    max_place = 0
    my_max = 0
    maxi = 0
    temp = True
    temp2 = False
    for i in range(1, len(seats)):
        if seats[i] != 0:
            temp = False
            if temp2 == False:
                temp2 = True
                maxi = i
                my_max = (max_place - 1) * 2 + 1

        if seats[i] == 0:
            max_place += 1
            if i == len(seats) - 1:
                if max_place - 1 > (my_max - 1) // 2 and temp == False:
                    seat[e] = i
                    seats[i] = e
                    return

        if seats[i] != 0:
            if (max_place - 1) // 2 > (my_max - 1) // 2:
                my_max = max_place
                maxi = i
            max_place = 0

    answer = maxi - ((my_max - 1) // 2) - ((my_max - 1) % 2) - 1

    if temp == True:
        answer = 1
    seat[e] = answer
    seats[answer] = e
    return


N, T, P = map(int, input().split())
people = []
for t in range(T):
    people.append(list(input().split()))

start_times = defaultdict(list)
end_times = defaultdict(list)

people.sort()
for t in range(T):
    if people[t][0] == people[t][1]:
        pass
    else:
        people[t][0] = int(people[t][0][:2]) * 60 + int(people[t][0][2:])
        people[t][1] = int(people[t][1][:2]) * 60 + int(people[t][1][2:])
        start_times[people[t][0]].append(t + 1)
        end_times[people[t][1]].append(t + 1)
answer = 0
seats = [0 for i in range(N + 1)]
seat = [0 for i in range(T + 1)]
for m in range(540, 1260):
    for e in end_times[m]:
        seats[seat[e]] = 0
        seat[e] = 0

    for e in start_times[m]:
        enter(e, seats, seat)

    if seats[P] == 0:
        answer += 1

print(answer)