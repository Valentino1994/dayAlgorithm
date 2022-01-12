def solution(N, Commands):

    now = [0, 0]

    for command in Commands:

        if command == "R" and now[1] < N:
            now[1] += 1
        elif command == "U" and now[0] > 0:
            now[0] -= 1
        elif command == "D" and now[0] < N:
            now[0] += 1
        elif command == "L" and now[1] > 0:
            now[1] -= 1

    return now[0]+1, now[1]+1

N = 5
Commands = ["R", "R", "R", "U", "D", "D"]
print(solution(N, Commands))