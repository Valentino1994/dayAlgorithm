import sys


def wind_move(graph, visited, x, y):
    global n, m

    ds = ((0, 1), (1, 0), (0, -1), (-1, 0))
    item = {1:(9, 1, 9, 3),
            2:(0, 9, 2, 9),
            3:(3, 2, 1, 0),
            4:(1, 0, 3, 2)}

    for i in range(4):
        d = ds[i]

        dx = x + d[0]
        dy = y + d[1]

        while True:
            # 연구실을 벗어나는 경우
            if 0 <= dx < n and 0 <= dy < m:
                # 현재 위치가 에어컨이 아닌 경우
                if graph[dx][dy] != 9:
                    visited[dx][dy] = True
                    # 현재 위치에 물건이 있는 경우
                    if graph[dx][dy] in (1, 2, 3, 4):
                        i = item[graph[dx][dy]][i]
                        # 물건1, 물건2로 인해 더 이상 이동하지 못하는 경우
                        if i == 9:
                            break
                        else:
                            d = ds[i]

                    dx += d[0]
                    dy += d[1]
                else:
                    break
            else:
                break
    return

def check_place(graph, air_conditioners):
    global n, m

    visited = [[False] * m for _ in range(n)]

    for x, y in air_conditioners:
        visited[x][y] = True

        wind_move(graph, visited, x, y)

    place_count = count_visit(visited)

    return place_count

def count_visit(visited):
    global n, m

    count = 0

    for i in range(n):
        for j in range(m):
            if visited[i][j]:
                count += 1

    return count

if __name__ == "__main__":
    sys.stdin = open("input.txt", "r")
    n, m = list(map(int, input().split()))

    graph = []
    air_conditioners = []

    for i in range(n):
        temp = list(map(int, input().split()))

        graph.append(temp)

        for j in range(m):
            if temp[j] == 9:
                air_conditioners.append((i, j))


    # print(*graph, sep='\n')
    # print(air_conditioner)

    print(check_place(graph, air_conditioners))