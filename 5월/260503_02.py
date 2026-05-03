from collections import deque

N = int(input())
A = [[] for _ in range(N+1)]

for _ in range(N):
    Data = list(map(int,input().split()))
    index = 0
    S = Data[index] # 첫번째 노드
    index += 1
    while True:
        E = Data[index] # 연결된 노드
        if E == -1:
            break # -1은 종료되었다는 의미
        V = Data[index+1] # 가중치 
        A[S].append((E,V)) # 연결된 노드와 가중치 추가
        index += 2 # 다음 연결된 노드로 이동

distance = [0] * (N + 1)
visited = [False] * (N + 1)

def BFS(V):
    queue = deque()
    queue.append(V)
    visited[V] = True  # 시작 노드 방문 처리 

    while queue:
        now_Node = queue.popleft()
        for i in A[now_Node]:
            if not visited[i[0]]:  # 방문 안한 노드만 탐색
                visited[i[0]] = True
                queue.append(i[0])
                distance[i[0]] = distance[now_Node] + i[1]

BFS(1)
Max = 1
for i in range(2, N+1):
    if distance[Max] < distance[i]:
        Max = i

distance = [0] * (N + 1)
visited = [False] * (N + 1)

BFS(Max)

print(max(distance))  # 가장 먼 거리 출력