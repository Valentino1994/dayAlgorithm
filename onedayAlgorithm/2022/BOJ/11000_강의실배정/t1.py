import sys
sys.stdin = open("input.txt")

n = int(input())
times = []
for _ in range(n):
    times.append(list(map(int, input().split(" "))))

sorted_time = sorted(times)

visited = [0 for _ in range(n)]
answer = 0
for i in range(n):
    if visited[i] == 0:
        now_time = sorted_time[i]
        visited[i] = 1
        answer += 1
        for j in range(i+1, n):
            next_time = sorted_time[j]
            if now_time[1] <= next_time[0]:
                visited[j] = 1

print(answer)