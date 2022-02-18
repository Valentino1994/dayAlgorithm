import sys
sys.stdin = open("input.txt", "r")

# 그리디는 시간초과난다..^^

N = int(input())

def stair_num(N):
    for i in range(1, len(N)-1):
        if abs(int(N[i]) - int(N[i-1])) != 1 or abs(int(N[i]) - int(N[i+1])) != 1:
            return False
    return True

if N == 1:
    print(9)

elif N == 2:
    print(17)

else:
    result = 0
    for i in range(10**(N-1), 10**N):
        if stair_num(str(i)):
           result += 1
    print(result % 1000000000)

