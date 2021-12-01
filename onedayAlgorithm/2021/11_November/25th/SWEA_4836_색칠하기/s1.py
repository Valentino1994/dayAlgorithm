import sys
sys.stdin = open("input.txt", 'r')

def coloring():

    # 빨간색과 파란색만 있음

    for coloring in coloring_info:

        # 색칠 인덱스는 0부터 시작함으로 따로 신경쓸 필요가 없음
        color = coloring[4]

        r1, r2 = coloring[0], coloring[2]
        c1, c2 = coloring[1], coloring[3]

        # 무조건 r2와 c2가 r1, c1보다 크다는 정보는 없음으로 아래의 값을 넣어준다.
        if r1 > r2:
            r1, r2 = coloring[2], coloring[1]
        if c1 > c2:
            c1, c2 = coloring[3], coloring[0]

        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                IN[i][j] += color

        result = 0
        for i in range(10):
            for j in range(10):
                # 같은 색인 영역은 겹치지 않기 때문에 겹치는 영역의 값은 무조건 3이 된다.
                if IN[i][j] == 3:
                    result += 1

    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # 격자의 모양은 10x10으로 고정되어 있다.
    IN = [ [0] * 10 for _ in range(10) ]
    # 색칠 정보를 받아온다.
    coloring_info = [ list(map(int, input().split())) for _ in range(N) ]

    print("#{} {}".format(tc, coloring()))