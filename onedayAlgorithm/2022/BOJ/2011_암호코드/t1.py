import sys
sys.stdin = open("input.txt")

password_code = list(input())
l = len(password_code)
DP = [0 for _ in range(l+1)]

if password_code[0] == '0':
    print(0)
else:
    password_code = [0] + password_code
    DP[0] = DP[1] = 1
    for i in range(2, len(password_code)):
        # 0이 들어올 경우에는 무조건 전 것과 합해야함.
        if int(password_code[i]) > 0:
            DP[i] += DP[i - 1]

        now_code = int(password_code[i-1] + password_code[i])
        if 10 <= now_code < 27:
            DP[i] += DP[i - 2]

    print(DP[-1] % 1000000)