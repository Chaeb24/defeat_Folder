from collections import deque

# 2606 바이러스
q = deque() 
visit = [0] * 100001 # visit 초기화

N = int(input()) # 컴퓨터 대수
M = int(input()) # 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수

graph = [[] for _ in range(N+1)] # 그래프 초기화
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b) # 양방향 연결
    graph[b].append(a)

def bfs(start):
    q.append(start)
    visit[start] = 1
    count = 0

    while q:
        node = q.popleft()
        
        for i in graph[node]:
            if visit[i] == 0: # 방문하지 않은 노드
                visit[i] = 1
                q.append(i)
                count += 1 # 감염된 컴퓨터 수 증가
    return count    

print(bfs(1)) # 1번 컴퓨터에서 시작
