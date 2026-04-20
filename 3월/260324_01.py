import sys

# 백준 2667

input = sys.stdin.readline
N = int(input()) # 몇 칸인가

houses = [list(input().strip()) for _ in range(N)] # 집 여부 
visit = [[False] * N for _ in range(N)]

house = []

def dfs(x,y):
    cnt = 1  # 단지 내 집 몇 개인가
    visit[x][y] = 1

    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    for i in range(4):
        cx = x + dx[i]
        cy = y + dy[i]

        if 0 <= cx < N and 0 <= cy < N and houses[cx][cy] == '1' and not visit[cx][cy]:
                cnt += dfs(cx,cy)
    return cnt
   
for i in range(N):
    for j in range(N):
        if houses[i][j] == '1' and not visit[i][j]:
            house.append(dfs(i, j))

house.sort()

print(len(house))
for h in house:
    print(h)       
