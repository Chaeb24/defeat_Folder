# 백준 2178 미로 탐색
from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int,input().split())

graph = [list(map(int,input().strip())) for _ in range(N)]
visit = [[0] * M for _ in range(N)] # 방문 여부 표시

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))
    visit[x][y] = 1

    while queue:
        x, y = queue.popleft()
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if nx <0 or ny<0 or nx >= N or ny >= M:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1: # nx, ny에 처음으로 이동했을 때에,
                graph[nx][ny] = graph[x][y] + 1 # graph[x][y]는 최소의 거리를 저장, 1을 더한 값을 graph[nx][ny]에 저장
                queue.append((nx,ny)) # 이동 된 nx, ny를 queue에 집어 넣기

    return graph[N-1][M-1] # 최종 n, m 위치에서의 graph 값 즉, 최소 거리를 반환함

print(bfs(0,0))


bfs(0, 0)




