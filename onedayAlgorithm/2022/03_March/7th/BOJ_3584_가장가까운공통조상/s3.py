import sys
sys.stdin = open("input.txt", "r")
def find_nodelist(node,tree):
    result=[node]
    while tree[node] != 0:
        result.append(tree[node])
        node=tree[node]
    return result

def solution():
    T=int(sys.stdin.readline())
    for _ in range(T):
        N=int(sys.stdin.readline())
        tree=[0]*(N+1)
        for _ in range(N-1):
            A,B=map(int,sys.stdin.readline().split())
            tree[B]=A
        node1, node2=map(int,sys.stdin.readline().split())

        node1_List=find_nodelist(node1,tree)
        node2_List=find_nodelist(node2,tree)

        # 뒤 부터 탐색 무조건 root 노드부터 이기 때문에
        pre=0
        for a,b in zip(node1_List[::-1],node2_List[::-1]):
            if a==b:
                pre=a
            else:
                print(pre)
                break
        else:
            print(pre)
solution()