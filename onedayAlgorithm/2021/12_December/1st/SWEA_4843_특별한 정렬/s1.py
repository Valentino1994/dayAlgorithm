import sys
sys.stdin = open("input.txt", "r")

def special_sort(AR):

    # 2중 for문을 돌리면서 시작 부분을 i로 바꾸면 해당 부분부터 끝까지의 최소값, 최대값을 구할 수 있다.
    for i in range(len(AR)):
        tmp_num = AR[i]
        idx = i
        for j in range(i, len(AR)):
            # 짝수 인덱스일 때는 최대값 홀수 인덱스일 때는 최소값
            if i % 2 == 0:
                if tmp_num < AR[j]:
                    tmp_num = AR[j]
                    idx = j
            else:
                if tmp_num > AR[j]:
                    tmp_num = AR[j]
                    idx = j

        AR[idx] = AR[i]
        AR[i] = tmp_num
    # 10개만 출력해야 한다.
    return AR[0:10]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    AR = list(map(int, input().split()))
    # join function은 string에만 사용할 수 있음으로 map 함수로 전부 바꿔서 join해준다.
    print("#{} {}".format(tc, " ".join(map(str, special_sort(AR)))))