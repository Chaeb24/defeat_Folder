import sys
input = sys.stdin.readline
from collections import deque

N, M, K, X = map(int,input().split())
visited = [-1] * (N + 1) # 방문 여부 처리
answer = []
A = [[] for _ in range(N+1)] # 그래프 데이터 저장 리스트

def BFS(v):
    queue = deque()
    queue.append(v) # 큐에 시작 노드 삽입
    visited[v] += 1
    
    while queue:
        now_Node = queue.popleft()
        for i in A[now_Node]:
            if visited[i] == -1:
                visited[i] = visited[now_Node] + 1
                queue.append(i)

for _ in range(M):
    S,E = map(int,input().split())
    A[S].append(E)

BFS(X)

for i in range(N+1):
    if visited[i] == K :
        answer.append(i)

if not answer:
    print(-1)
else:
    answer.sort()
    for i in answer:
        print(i)