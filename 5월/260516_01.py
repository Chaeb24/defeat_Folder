import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
isEven = True

def DFS(v):
    global isEven
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            check[i] = (check[v]+1)%2 
            # 자신과 연결된 노드는 다른 번호로 넘버링
            DFS(i)
        elif check[v] == check[i]:
            isEven = False

for _ in range(N): # 테스트케이스만큼 입력받기
    V,E = map(int,input().split()) #노드와 엣지
    A = [[] for _ in range(V+1)]
    visited = [False] * (V+1)
    check = [0] * (V+1)
    isEven = True

    for i in range(E):
        S, E = map(int,input().split())
        A[S].append(E)
        A[E].append(S)

    for i in range(1,V+1): #노드개수만큼 이분그래프실행
        if isEven:
            DFS(i)
        else:
            break
    # 이분그래프이면 출력값
    if isEven:
        print("YES")
    else:
        print("NO")