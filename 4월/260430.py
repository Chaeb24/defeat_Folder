# 백준 11724
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n,m = int(input().split()) # 노드와 엣지 개수 입력
visited = [False] * (n+1)
A = [[] for _ in range(n+1)]

def DFS(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)

for _ in range(m):
    s,e = map(int,input().split())
    A[s].append(e)
    A[e].append(s)

count = 0

for i in range(1,n+1):
    if not visited[i]:
        count += 1
        DFS(i)

print(count)





