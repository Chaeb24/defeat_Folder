import sys
from collections import deque

# 백준 10026

input = sys.stdin.readline
tc = int(input()) # 테스트 케이스 수

graph = [list(input().strip()) for _ in range(tc)]

def bfs(x,y,visit):
    q = deque()
    q.append((x,y))
    visit[x][y] = 1

    while q:
        x, y = q.popleft()

        nx, ny = [1, -1, 0, 0], [0, 0, 1, -1]

        for i in range(4):
            cx,cy = x +nx[i], y + ny[i]

            if 0 <= cx < tc and 0 <= cy < tc and not visit[cx][cy] and graph[x][y] == graph[cx][cy]:
                visit[cx][cy] = 1
                q.append((cx,cy))

# 일반인 경우
ans = [0,0]
visit = [[False] * tc for _ in range(tc)] # 방문여부 확인

for i in range(tc):
    for j in range(tc):
        if not visit[i][j]:
            bfs(i,j,visit)
            ans[0] +=1

# 적록색약인 경우
visited = [[False] * tc for _ in range(tc)]

for i in range(tc):
    for j in range(tc):
            if graph[i][j] == 'G':
                graph[i][j] = 'R'

for i in range(tc):
    for j in range(tc):
        if visited[i][j] == False:
            bfs(i,j,visited)
            ans[1] += 1

print(' '.join(map(str, ans)))

