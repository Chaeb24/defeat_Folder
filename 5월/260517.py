from collections import deque

# A,B,C의 경우의 수를 따져서 경로 설정
Sender = [0,0,1,1,2,2]
Receiver = [1,2,0,2,0,1]
now = list(map(int,input().split()))
visited = [[False for j in range(201)] for i in range(201)]
answer = [False] * 201

def BFS():
    queue = deque()
    queue.append((0,0)) # A,B 물통 저장
    visited[0][0] = True
    answer[now[2]] = True
    while queue:
        now_Node = queue.popleft()
        A = now_Node[0]
        B = now_Node[1]
        C = now[2] - A - B
        for k in range(6):
            next = [A,B,C]
            next[Receiver[k]] += next[Sender[k]] # 이미 물을 받았음.
            next[Sender[k]] = 0
            if next[Receiver[k]] > now[Receiver[k]]: # 넘치면
                next[Sender[k]] = next[Receiver[k]] - now[Receiver[k]] # 넘치는 만큼 받기
                next[Receiver[k]] = now[Receiver[k]] # 최대 용량만 받음.
            if not visited[next[0]][next[1]]:
                visited[next[0]][next[1]] = True
                queue.append((next[0],next[1]))
                if next[0] == 0:
                    answer[next[2]] = True

BFS()

for i in range(len(answer)):
    if answer[i]:
        print(i,end = ' ')