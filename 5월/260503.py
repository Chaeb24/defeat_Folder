# DFS, BFS 둘 다 구현
from collections import deque # BFS 사용
N, M, Start = map(int, input().split()) # 노드, 엣지, 시작점
A = [[] for _ in range(N+1)]

for _ in range(M): 
    s,e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

for i in range(N+1):
    A[i].sort()

def DFS(v):
    print(v, end = ' ')
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)

visited = [False] * (N+1)
DFS(Start)

def BFS(v):
    queue = deque()
    queue.append(v)
    visited[v] = True
    while queue:
        now_Node = queue.popleft() # 큐에서 하나 빼기
        print(now_Node, end = ' ') # 큐에서 뽑은 노드 출력
        for i in A[now_Node]:
            if not visited[i]: # 노드랑 연결된 다른 노드 확인
                visited[i] = True
                queue.append(i)

print()
visited = [False] * (N+1) # 리스트 초기화
BFS(Start)



