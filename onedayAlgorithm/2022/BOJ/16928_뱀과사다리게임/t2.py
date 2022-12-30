import sys
sys.stdin = open("input.txt")

N, M = list(map(int, input().split(" ")))
ladder = dict()
snake = dict()

for _ in range(N):
    s, e = list(map(int, input().split(" ")))
    ladder[s] = e

for _ in range(M):
    s, e = list(map(int, input().split(" ")))
    snake[s] = e

board = [0 for _ in range(101)]
visited = [False for _ in range(101)]

def bfs():
    queue = [[1, 0]] # position, count
    queue_index = 0

    while len(queue) > queue_index:
        position, count = queue[queue_index]
        for i in range(1, 7):
            next_position = position + i
            next_position = whereIsNext(next_position)

            if next_position <= 100 and not visited[next_position]:
                board[next_position] = count + 1
                visited[next_position] = True
                queue.append([next_position, count + 1])

        queue_index += 1

    return

def whereIsNext(next_position):
    result = next_position

    if next_position in ladder.keys():
        result = ladder[next_position]
        return result

    if next_position in snake.keys():
        result = snake[next_position]
        return result

    return result

bfs()
print(board[100])