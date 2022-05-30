def solution(n, times):
    answer = 0
    if n == 1:
        return answer

    DP = [0] * (n + 1)
    # when we start to cut, we should cut from a one line.
    DP[2] = times[0]

    for i in range(2, n+1):
        # If the i is an odd number, there is only one way to make it
        if i % 2 != 0:
            DP[i] = DP[i-1] + times[0]
            continue
        # If the i is not an odd number, there is two ways to make it
        # I should to choice the min value from that
        DP[i] = min(DP[i-1]+times[0], DP[i//2]+times[i//2-1])

    answer = DP[n]

    return answer

n = 2
times = [2]

print(solution(n, times))