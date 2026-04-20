import sys

input = sys.stdin.readline

N = int(input()) # 몇 칸인지

graph = [list(map(int, input().split())) for _ in range(N)] # 갈 수 있는 거리 저장
dp = [[0] * N for _ in range(N)] # 방문한 지점 저장용 배열
dp[0][0] = 1


for x in range(N):
    for y in range(N):
        if dp[x][y] == 0:
            continue

        if x == N-1 and y == N-1:
            continue

        jump = graph[x][y]

        if x + jump < N:
            dp[x+jump][y] += dp[x][y]
        
        if y + jump < N:
            dp[x][y+jump] += dp[x][y]

print(dp[N-1][N-1])


   
    

