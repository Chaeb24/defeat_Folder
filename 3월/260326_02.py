import sys
from collections import deque

input = sys.stdin.readline
R,C = map(int,input().split()) # R행 C열로 입력 받음
# 백준 3055
# 지도 입력 받음.
graph = [list(input().strip()) for _ in range(R)]
visit = [[-1] * C for _ in range(R)]

# *은 물이고, X은 돌
# S가 현재위치이고 D로 이동하는게 목표

dy = [1,-1,0,0]
dx = [0,0,1,-1]

q = deque()

# 물이랑 고슴도치는 움직이는 애들
for y in range(R):
    for x in range(C):
        if graph[y][x] == '*': # 물을 만난 경우
            q.appendleft((y,x))
        elif graph[y][x] == 'S': # 시작점 만난 경우
            q.append((y,x))
            visit[y][x] = 0

while q :
    y,x = q.popleft()
    cur = graph[y][x]

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if ny < 0 or ny >= R or nx < 0 or nx >= C:  # 범위 밖이면 무시
            continue
        if visit[ny][nx] != -1:
            continue
        if graph[ny][nx] == '*': # 물을 만났으면
            continue
        if graph[ny][nx] == 'X': # 돌을 만났으면
            continue
        if cur == "*" and graph[ny][nx] == "D":  # 물이 비버네 가려면 무시
            continue

        if cur == "S":
            if graph[ny][nx] == "D":  # 고슴이가 가려는 위치가 비버네면 도착
                print(visit[y][x] + 1)
                break
            visit[ny][nx] = visit[y][x] + 1  # 비버네가 아니면 도착 시간 기록

        graph[ny][nx] = cur  # 다음 좌표를 고슴이 or 물로 변경
        q.append((ny, nx))  # 다음 탐색 위치 추가
    else:
        continue
    break
else:
    print("KAKTUS")
    

