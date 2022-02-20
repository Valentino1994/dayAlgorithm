import sys
input = sys.stdin.readline
# N: 점의 갯수, N-1:간선의 수, R: 루트 노드, Q:쿼리 횟수
N, R, Q = map(int,input().split())
# 인접리스트 및 작성(1->0으로 하여 0부터 시작하게 설정했다.)
adjlist = [[] for _ in range(N)]
for i in range(N-1):
    u, v = map(int,input().split())
    adjlist[u-1].append(v-1)
    adjlist[v-1].append(u-1)
# 정점에서 이어진 길이 있는지 확인 여부.
onoff = [True]*N
# DFS Post Order Traversal: 리프 노드 -> 루트 노드
# 후위 순회를 위한 스택. 루트 노드부터 시작한다.
checklist = [R-1]
postOrder = []
while checklist:
    # 스택의 마지막 정점을 확인한다.
    x = checklist[-1]
    onoff[x] = False
    isleaf = True
    # x -> y x와 이어진 정점들을 모두 확인하면서
    for y in adjlist[x]:
        # 아직 확인하지 않은 정점이라면 확인할 리스트에 넣은 뒤 리프 노드가 아님을 표시한다.
        if onoff[y] :
            checklist.append(y)
            isleaf = False
    # 리프 노드였다면 스택에서 빼내어 순회 순서 목록에 넣는다.
    if isleaf : postOrder.append(checklist.pop())
# 서브트리 점의 개수. 자기자신을 포함하므로 최소 1개
subTree_nV = [1]*N
# 순회 순서대로 전부 체크해가며 연결된 부모 노드에 자식 노드 합을 더해준다.
for x in postOrder:
    for node in adjlist[x]:
        if not onoff[node]: subTree_nV[node]+=subTree_nV[x]
    onoff[x] = True
print(*[subTree_nV[int(input())-1] for _ in range(Q)])