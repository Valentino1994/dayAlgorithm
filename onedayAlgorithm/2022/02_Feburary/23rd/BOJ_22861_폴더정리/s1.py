import sys
sys.stdin = open("input.txt", "r")

N, M = map(int, input().split())

folder = {}

for _ in range(N+M):
    P, F, C = input().split()
    if P not in folder:
        folder[P] = [[], []]
    if C == "1":
        folder[P][0].append(F)
    else:
        folder[P][1].append(F)

K = int(input())
for _ in range(K):
    info = input().split()
    start = info[0].split("/")
    destination = info[1].split("/")

    # s1은 s2에서 없어져야할 것
    s1, s2 = start[-1], start[-2]
    # d1은 s1에서 가져온 파일들이 저장되야할 곳
    d1, d2 = destination[-1], destination[-2]

    for fold in folder[s1][0]:
        folder[d1][0].append(fold)

    for file in folder[s1][1]:
        if file not in folder[d1][1]:
            folder[d1][1].append(file)

    folder[s2][0].remove(s1)
    folder.pop(s1)

Q = int(input())
for _ in range(Q):
    # r1은 파일의 개수 r2는 파일의 종류
    r1 = 0
    r2 = set()

    start_point = input().split('/')
    stack = [start_point[-1]]

    while stack:
        now_folder = stack.pop()
        # 현재의 폴더 개수를 더해주고.
        r1 += len(folder[now_folder][1])
        # # 폴더 종류를 더하기 위해 차례대로 r2에 add해준다.
        for file in folder[now_folder][1]:
            r2.add(file)

        for fold in folder[now_folder][0]:
            stack.append(fold)
    print(r1, len(r2))
