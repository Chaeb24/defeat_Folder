import sys
from collections import deque

input = sys.stdin.readline
# 유기농 배추 문제

def bfs(x,y,visit):
    q = deque()
    q.append((x,y))
    visit[x][y] = 1

    nx = [1,-1,0,0]
    ny = [0,0,1,-1]

    while q :
        x,y = q.popleft()

        for i in range(4):
            cx = x + nx[i]
            cy = y + ny[i]
        
            if 0<= cx < N and 0<= cy < M and not visit[cx][cy] and graph[cx][cy] == 1:
                visit[cx][cy] = 1
                q.append((cx,cy))


T = int(input()) # 테스트케이스 수
for _ in range(T): # 테스트케이스 수 만큼
    M, N, K = map(int, input().split()) # 가로, 세로, 위치 개수

    graph = [[0] * M for _ in range(N)] # 땅의 구조
    visit = [[0] * M for _ in range(N)] # 방문 여부
    cnt = 0

    for _ in range(K):
        a,b = map(int,input().split()) # 좌표
        graph[b][a] = 1 # 좌표 입력 시키기
    
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1 and not visit[i][j]:
                bfs(i,j,visit)
                cnt += 1

    print(cnt)


    
   
