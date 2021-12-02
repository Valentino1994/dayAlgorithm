import sys
sys.stdin = open("input.txt", "r")

def binary_search(P, A, B):
    # 첫 시작은 항상 끝에서 끝이다.
    A_left = B_left = 1
    A_right = B_right = P
    # 찾을 때까지 반복한다.
    while True:

        A_center = (A_left + A_right) // 2
        B_center = (B_left + B_right) // 2
        # 동시에 center에 도착했다면 비긴다.
        if A == A_center and B == B_center:
            return 0
        elif A_center == A:
            return 'A'
        elif B_center == B:
            return 'B'

        # 중간값이 현재값보다 크면 오른쪽을 땡겨서 가운데에 맞춘다는 이미지.
        if A_center > A:
            A_right = A_center
        else:
            A_left = A_center

        if B_center > B:
            B_right = B_center
        else:
            B_left = B_center

T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    print("#{} {}".format(tc, binary_search(P, A, B)))