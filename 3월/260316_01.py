# 1260 백준
from collections import deque

N, M, V = map(int, input().split())
# 노드, 간선, 시작점


visit = [0] * 10001 # dfs용
visit1 = [0] * 10001 # bfs 용
graph = [ [False] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1


def dfs(start):
    
    visit[start] = 1 # 방문함 체크
    print(start, end=' ')

    for i in range(1,N+1): # 방문 안했고, 그래프로 연결되어있으면
        if visit[i] == 0 and graph[start][i]:
            dfs(i)

    
def bfs(start):
    q = deque([start])
    visit1[start] = 1 # 방문함 체크
    
    while q: # 큐에 입력된 값들 확인
        node = q.popleft()
        print(node,end = ' ')

        for i in range(1,N+1):# 방문 안했고, 그래프로 연결되어있으면
            if visit1[i] == 0 and graph[node][i]:
                q.append(i)
                visit1[i] = 1
                
dfs(V)
print()
bfs(V)    
