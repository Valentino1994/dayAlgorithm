def solution(T):
    sCount = 0
    mCount = 0
    lCount = 0

    for i in range(len(T)):
        if T[i] == "S":
            sCount += 1
        elif T[i] == "M":
            mCount += 1
        else:
            lCount += 1

    return ("S" * sCount) + ("M" * mCount) + ("L" * lCount)

T = "SMS"
print(solution(T))
