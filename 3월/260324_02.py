import sys

input = sys.stdin.readline
N = int(input())

# 11403 백준

graph = [list(map(int, input().split())) for _ in range(N)]

def dfs(x):
    for i in range(N): # 옆으로 갈 수 있는지 여부만 알면 됨.
        if graph[x][i] == 1 and visit[i] == 0:
            visit[i] = 1
            dfs(i)


for i in range(N):
    visit = [0 for _ in range(N)]
    dfs(i)
    for j in range(N):
        if visit[j] == 1:
            print(1, end=' ')
        else:
            print(0, end=' ')
    print()
