import sys
sys.stdin = open("input.txt")

from collections import deque
N,M = map(int,input().split())
arr = []        ## map을 복사 ~~
land = []       ## 땅이 있는 곳의 좌표만 저장 ~~
for i in range(N):
    arr.append(list(input()))
    for j in range(M):
        if arr[i][j] == 'L':
            land.append((i,j))
dx,dy = [0,1,0,-1], [1,0,-1,0]
## 땅이 있는 곳들의 배열인 land에서 하나씩 꺼내서 최단거리만 저장하며 완전탐색하는 bfs진행
def bfs(x,y):
    queue = deque([(x,y)])  # 하나 꺼낸 땅 좌표 넣고
    temp = 0                # 더이상 앞으로 못가면 바로 최장거리인지 계속 확인하기 위해서
    visited = [[0]*M for _ in range(N)]  # 거리 저장 및 visited
    # visited[x][y] = 1 ###########################################이곳?
    while queue:
        x,y = queue.popleft()
        ck = True           # 어디로 이동 못했는지 체크하기 위해서
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            if 0<=nx<N and 0<=ny<M and arr[nx][ny] == 'L' and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1 # 이동 전 좌표에서 +1 해줌
                queue.append((nx,ny))
                ck = False
        if ck: temp = max(temp,visited[x][y]) # 동서남북 봤는데 아무데도 못갔으면 최대값인지 확인
        # if ck: temp = max(temp,visited[x][y]-1) #################################위에서 1로 시작해서..
    return temp     # 최장거리 반환

rtn = 0
for lan in land:       # 땅 좌표 하나씩 bfs 실행
    x,y = lan
    ans = bfs(x,y)  # 최장거리 받고
    rtn = max(ans,rtn)  #  이번 땅에서의 최장거리가 전체 땅 좌표 중에서도 최장인지 확인
print(rtn)