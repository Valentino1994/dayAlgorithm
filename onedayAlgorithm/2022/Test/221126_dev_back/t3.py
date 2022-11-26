def solution(subway, start, end):
    new_subway = []
    for i in range(len(subway)):
        new_subway.append(list(map(int, subway[i].split(" "))))

    visited = [0 for _ in range(len(new_subway))]
    answer = 987654321

    def dfs(cnt, now_line, now_path):
        nonlocal answer

        if answer <= cnt:
            return
        if end in new_subway[now_line]:
            answer = min(answer, cnt)
            return

        for i in range(len(new_subway[now_line])):
            now_station = new_subway[now_line][i]
            for j in range(len(new_subway)):
                if now_station in new_subway[j] and now_station not in now_path:
                    now_path.append(now_station)
                    dfs(cnt + 1, j)
                    now_path.pop()

    for i in range(len(new_subway)):
        now_subway = new_subway[i]
        for j in range(len(now_subway)):
            if now_subway[j] == start:
                visited[i] = 1
                dfs(0, i)

    if answer == 987654321:
        answer = -1

    return answer

subway = ["1 2 3 4 5 6 7 8 9 10", "2 8"]
start = 1
end = 10
subway1 = ["1 2 3 4 5 6 7 8", "2 11", "0 11 10", "3 17 19 12 13 9 14 15 10", "20 2 21"]
start1 = 1
end1 = 9
subway2 = ["0 1 2 3 4", "1 12 13 14"]
start2 = 2
end2 = 12
print(solution(subway, start, end))
print(solution(subway1, start1, end1))
print(solution(subway2, start2, end2))