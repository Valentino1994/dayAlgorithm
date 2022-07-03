def solution(n, horizontal):
    answer = [[]]

    now_direction = horizontal
    now_count = 1

    room = [ [0] * n for _ in range(n) ]
    room[0][0] = 1
    now_r, now_c = 0, 0

    # 현재 범위가 무조건 n 안쪽에 있어야함
    while now_r < n - 1 and now_c < n - 1:

        # 만약 현재 horizontal이면 now_range만큼 아래로 내려왔다가 now_range만큼 왼쪽으로 이동함.
        if now_direction:
            # 먼저 한 칸 오른쪽으로 이동시키고 찍어줌
            now_c += 1
            now_count += 1
            room[now_r][now_c] = now_count
            while now_c > now_r:
                now_r += 1
                now_count += 1
                room[now_r][now_c] = now_count

            while now_c > 0:
                now_c -= 1
                now_count += 1
                room[now_r][now_c] = now_count

            now_direction = False

        # 만약 현재 vertical이면 now_range만큼 오른쪽으로 갔다가 위쪽으로 이동함.
        else:
            now_r += 1
            now_count += 1
            room[now_r][now_c] = now_count
            while now_c < now_r:
                now_c += 1
                now_count += 1
                room[now_r][now_c] = now_count

            while now_r > 0:
                now_r -= 1
                now_count += 1
                room[now_r][now_c] = now_count

            now_direction = True

    answer = room

    return answer


n = 4
horizontal = True

print(solution(n, horizontal))
