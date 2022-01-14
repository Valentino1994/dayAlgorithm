import sys
sys.stdin = open("input.txt", "r")
#input = sys.stdin.readline
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

def solution(arr):
    meetings = sorted(arr)
    max_meetings = [meetings[0]]

    for i in range(1, N):

        prev_meeting = max_meetings[-1]
        now_meeting = meetings[i]

        # 만약 더 빨리 끝난다면 이유 불문 바꾼다.
        if prev_meeting[1] > now_meeting[1]:
            max_meetings[-1] = now_meeting
            continue

        # 빨리 끝나지 않는데 시간이 겹치지 않는다면 추가한다.
        if prev_meeting[1] <= now_meeting[0]:
            max_meetings.append(now_meeting)

    return max_meetings

print(solution(arr))
