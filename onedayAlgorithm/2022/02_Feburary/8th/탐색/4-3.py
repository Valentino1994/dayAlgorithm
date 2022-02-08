s = "c2"

n_r, n_c = int(s[1]), (ord(s[0]) - 96)

movement = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [-1, 2], [1, -2], [-1, -2]]

cnt = 0
for move in movement:
    r = n_r + move[0]
    c = n_c + move[1]
    if 0 < r < 9 and 0 < c < 9:
        cnt += 1

print(cnt)