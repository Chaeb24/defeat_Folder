import sys
input = sys.stdin.readline
N,M = map(int,input().split())
edges = []
distance = [sys.maxsize] * (N+1)

for i in range(M):
    start,end, time = map(int,input().split())
    edges.append((start,end,time))

distance[1] = 0 #벨만포드

for _ in range(N-1):
    for start,end,time in edges:
        if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
            distance[end] = distance[start] + time # 거리가 짧은걸로 업데이트

mCycle = False

for start,end,time in edges:
    if distance[start] != sys.maxsize and distance[end] > distance[start] + time:
        mCycle = True # 가중치에 음수가 있다는 걸 확인

if not mCycle:
    for i in range(2, N+1):
        if distance[i] != sys.maxsize:
            print(distance[i])
        else:
            print(-1)
else:
    print(-1)