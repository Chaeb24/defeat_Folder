import sys
from collections import deque

input = sys.stdin.readline
# 백준 7562
def bfs(x,y,z,w):
    q = deque()
    q.append((x,y)) # 큐에 추가 시 튜플 형식으로
    visit = [[0] * I for _ in range(I)] # 체스판 방문 여부

    dx = [2, 2, -2, -2, 1, 1, -1, -1] # 나이트 움직이는 경우의 수 전부 생각
    dy = [1, -1, 1, -1, 2, -2, 2, -2]

    while q:
        x,y = q.popleft()

        if x == z and y == w:  # 방문 완료한 경우
            return visit[x][y] # 누적된 횟수 반환
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < I and 0 <= ny < I and not visit[nx][ny]:
                visit[nx][ny] = visit[x][y] + 1 # 거리 누적, 방문 여부 아님.
                q.append((nx, ny))


T = int(input()) # 테스트 케이스 수

for _ in range(T):
    I = int(input()) # 체스판 길이
    a,b = map(int,input().split()) # 체스판에서 현재 위치
    c,d = map(int,input().split()) # 체스판에서 이동하려는 위치

    res = bfs(a,b,c,d)
    print(res)
