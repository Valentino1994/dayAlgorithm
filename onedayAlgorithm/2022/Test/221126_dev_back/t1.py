def solution(low, high, img):
    # img 안에 접근할 수 있어야함
    def check_black(start, batch_size, N):
        r, c = start
        if r + batch_size > N or c + batch_size > len(img[0]):
            return False

        # 사각형의 윗변
        for i in range(batch_size):
            if img[r][c + i] == ".":
                return False
        # 사각형의 아랫변
        for i in range(batch_size):
            if img[r + batch_size - 1][c + i] == ".":
                return False
        # 사각형의 좌변
        for i in range(batch_size):
            if img[r + i][c] == ".":
                return False
        # 사각형의 우변
        for i in range(batch_size):
            if img[r + i][c + batch_size - 1] == ".":
                return False

        return True

    def cal_portion(start, batch_size):
        # 가장자리는 제외하기 때문에 가장자리의 대각선 아래부터 시작.
        r = start[0] + 1
        c = start[1] + 1
        # 왼쪽에서 한칸, 오른쪽에서 한칸 줄어들었음
        black = 0
        for i in range(batch_size - 2):
            for j in range(batch_size - 2):
                if img[r + i][c + j] == "#":
                    black += 1

        return int((black / (batch_size-2) ** 2) * 100)

    answer = 0
    batch_size = len(img) # 현재부터 batch_size는 3부터 시작함.
    N = len(img)
    while batch_size >= 3:
        # 매 batch_size마다 img를 새롭게 봐줘야함
        for i in range(N):
            for j in range(len(img[0])):
                # 가장자리가 무조건 검은색이여야함으로 검은색일때 시작함
                if img[i][j] == "#":
                    if check_black([i, j], batch_size, N):
                        # 위에서 이미 벽을 체크했음으로 비율을 계산할 때는 벽을 체크할 필요가 없음.
                        now_portion = cal_portion([i, j], batch_size)

                        if low <= now_portion < high:
                            answer += 1
        batch_size -= 1

    return answer


low = 25
high = 51
img = [".########......", ".####...#......", ".#.####.#.#####", ".#.#..#.#.#..##", ".#.##.#.#.#...#", ".#.####.#.#...#", ".#....###.#####", ".########......"]
print(solution(low, high, img))