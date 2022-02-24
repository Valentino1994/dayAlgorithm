import sys
sys.stdin = open("input.txt", "r")

def solution(maps, r, c):
    answer = 0
    arduino = []
    x, y = 0, 0
    dx = [0, 1, 1, 1, 0, 0, 0, -1, -1, -1]
    dy = [0, -1, 0, 1, -1, 0, 1, -1, 0, 1]

    for i in range(r):
        for j in range(c):
            if maps[i][j] == 'R':
                arduino.append([i, j])
            elif maps[i][j] == 'I':
                x, y = i, j

    for move in moves:
        nx = x + dx[move]
        ny = y + dy[move]

        answer += 1

        if maps[nx][ny] == 'R':
            return print("kraj %d" % answer)

        maps[x][y] = '.'
        maps[nx][ny] = 'I'
        x, y = nx, ny

        ard_maps = [[0] * c for _ in range(r)]
        for i, ard in enumerate(arduino):
            if x > ard[0]:
                ard[0] += 1
            if x < ard[0]:
                ard[0] -= 1
            if y > ard[1]:
                ard[1] += 1
            if y < ard[1]:
                ard[1] -= 1

            if maps[ard[0]][ard[1]] == 'I':
                return print("kraj %d" % answer)
            else:
                ard_maps[ard[0]][ard[1]] += 1

        new_arduino = []
        for i in range(r):
            for j in range(c):
                maps[i][j] = '.'
                if ard_maps[i][j] == 1:
                    new_arduino.append([i, j])
                    maps[i][j] = 'R'
                elif i == x and j == y:
                    maps[i][j] = 'I'
        arduino = new_arduino

    for i in range(r):
        print(''.join(maps[i]))
    return


r, c = map(int, input().split())
maps = [list(map(str, input())) for _ in range(r)]
moves = list(map(int, input()))
solution(maps, r, c)