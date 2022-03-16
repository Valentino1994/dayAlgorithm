import sys
sys.stdin = open("input.txt", "r")

info = list(map(int, input().split()))
cube_vl = []
cube_vr = []
cube_hu = []
cube_hd = []

for i in range(12):
    if i % 2 == 0:
        cube_vl.append(info[i])
    else:
        cube_vr.append(info[i])
for i in range(12, len(info), 2):
    if i % 4 == 0:
        cube_hu.extend([info[i], info[i+1]])
    else:
        cube_hd.extend([info[i], info[i+1]])

cube_vl.extend([cube_hu[5], cube_hd[5]])
cube_vr.extend([cube_hu[4], cube_hd[4]])
cube_hu.insert(2, cube_vl[4])
cube_hu.insert(3, cube_vr[4])
cube_hd.insert(2, cube_vl[5])
cube_hd.insert(3, cube_vr[5])

def turn(index):
    ncube_vl = cube_vl
    ncube_vr = cube_vr
    ncube_hu = cube_hu
    ncube_hd = cube_hd
    # 상좌 : vertical 의 짝수 인덱스를 한칸 위로 (0, 2일 때만 12, 14로 나머지는 -2씩 해줌)
    if index == 0:
        ncube_vl = ncube_vl[2:] + ncube_vl[:2]
        ncube_hu = ncube_hu[:2] + ncube_vl[4:5] + ncube_vr[4:5] + ncube_hu[4:6] + ncube_vr[1:2] + ncube_vl[0:1]
        ncube_hd = ncube_hd[:2] + ncube_vl[5:6] + ncube_vr[5:6] + ncube_hd[4:6] + ncube_vr[1:2] + ncube_vr[0:1]
        return [ncube_vl, ncube_vr, ncube_hu, ncube_hd]
    # 상우
    elif index == 1:
        ncube_vr = ncube_vr[2:] + ncube_vr[:2]
        ncube_hu = ncube_hu[:2] + ncube_vl[4:5] + ncube_vr[4:5] + ncube_hu[4:6] + ncube_vr[1:2] + ncube_vl[0:1]
        ncube_hd = ncube_hd[:2] + ncube_vl[5:6] + ncube_vr[5:6] + ncube_hd[4:6] + ncube_vr[1:2] + ncube_vr[0:1]
        return [ncube_vl, ncube_vr, ncube_hu, ncube_hd]
    # 하좌
    elif index == 2:
        ncube_vl = ncube_vl[4:] + ncube_vl[:4]
        ncube_hu = ncube_hu[:2] + ncube_vl[4:5] + ncube_vr[4:5] + ncube_hu[4:6] + ncube_vr[1:2] + ncube_vl[0:1]
        ncube_hd = ncube_hd[:2] + ncube_vl[5:6] + ncube_vr[5:6] + ncube_hd[4:6] + ncube_vr[1:2] + ncube_vr[0:1]
        return [ncube_vl, ncube_vr, ncube_hu, ncube_hd]
    # 하우
    elif index == 3:
        ncube_vr = ncube_vr[4:] + ncube_vr[:4]
        ncube_hu = ncube_hu[:2] + ncube_vl[4:5] + ncube_vr[4:5] + ncube_hu[4:6] + ncube_vr[1:2] + ncube_vl[0:1]
        ncube_hd = ncube_hd[:2] + ncube_vl[5:6] + ncube_vr[5:6] + ncube_hd[4:6] + ncube_vr[1:2] + ncube_vr[0:1]
        return [ncube_vl, ncube_vr, ncube_hu, ncube_hd]
    # 상좌
    elif index == 4:
        ncube_hu = ncube_hu[2:] + ncube_hu[:2]
        ncube_vl[1] = ncube_hu[6]
        ncube_vr[1] = ncube_hu[7]
        ncube_vl[4] = ncube_hu[2]
        ncube_vr[4] = ncube_hu[3]
        return [ncube_vl, ncube_vr, ncube_hu, ncube_hd]
    # 하좌
    elif index == 5:
        ncube_hd = ncube_hd[2:] + ncube_hd[:2]
        ncube_vl[0] = ncube_hd[6]
        ncube_vr[0] = ncube_hd[7]
        ncube_vl[5] = ncube_hd[2]
        ncube_vr[5] = ncube_hd[3]
        return [ncube_vl, ncube_vr, ncube_hu, ncube_hd]
    # 상우
    elif index == 6:
        ncube_hu = ncube_hu[4:] + ncube_hu[:4]
        ncube_vl[1] = ncube_hu[6]
        ncube_vr[1] = ncube_hu[7]
        ncube_vl[4] = ncube_hu[2]
        ncube_vr[4] = ncube_hu[3]
        return [ncube_vl, ncube_vr, ncube_hu, ncube_hd]
    # 하우
    elif index == 7:
        ncube_hd = ncube_hd[4:] + ncube_hd[:4]
        ncube_vl[0] = ncube_hd[6]
        ncube_vr[0] = ncube_hd[7]
        ncube_vl[5] = ncube_hd[2]
        ncube_vr[5] = ncube_hd[3]
        return [ncube_vl, ncube_vr, ncube_hu, ncube_hd]

def check(cube):

    cube_vl = cube[0]
    cube_vr = cube[1]
    cube_hu = cube[2]
    cube_hd = cube[3]

    for i in range(0, len(cube_vl), 2):
        if not (cube_vr[i] == cube_vr[i+1] == cube_vl[i] == cube_vl[i+1] and cube_hu[i] == cube_hu[i+1] == cube_hd[i] == cube_hd[i+1]):
            return 0

    return 1

flag = False
for t in range(8):
    cube = turn(t)
    if check(cube) == 1:
        flag = True

if flag:
    print(1)
else:
    print(0)
