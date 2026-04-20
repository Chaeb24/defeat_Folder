import sys

input = sys.stdin.readline
N = int(input())  # 격자 개수
# 백준 14520
graph = [list(map(int, input().split())) for _ in range(N)]
visit = [[False] * N for _ in range(N)]
dx, dy = [0, 1, -1, 0, 0], [0, 0, 0, 1, -1] # 꽃을 심기위한 비용

cnt = 0 # 3번 심었는지 확인
cost = 0
ans = 10001

def check(x, y):
    for i in range(5):
        nx = x + dx[i]
        ny = y + dy[i]

        if visit[ny][nx]:
            return False
    return True

def dfs():
    global cnt, cost, ans

    if cnt == 3:
        ans = min(ans, cost)
        return

    for row in range(1, N - 1):
        for col in range(1, N - 1):
            if check(col, row):
                cnt += 1

                for d in range(5):
                    nx = col + dx[d]
                    ny = row + dy[d]
                    visit[ny][nx] = True
                    cost += graph[ny][nx]

                dfs()

                cnt -= 1
                for d in range(5):
                    nx = col + dx[d]
                    ny = row + dy[d]
                    visit[ny][nx] = False
                    cost -= graph[ny][nx]

dfs()
print(ans)