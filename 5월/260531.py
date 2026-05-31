import sys
from collections import deque
input = sys.stdin.readline

n = int(input()) # 도시 수
m = int(input()) # 도로 수
cityList = [[] for _ in range(n+1)] # 도시 수 만큼 입력 받기
revcityList = [[] for _ in range(n+1)] # 역방향 리스트
indegree = [0] * (n+1)

for i in range(m):
    S,E,V = map(int,input().split())
    cityList[S].append((E,V)) 
    revcityList[E].append((S,V)) # 역방향 리스트에 저장
    indegree[E] += 1 # 진입차수 리스트 (E랑 연결된 개수만큼)

start,end = map(int,input().split()) # 시작,도착 도시 데이터

queue = deque()
queue.append(start) # 출발 도시를 큐에 삽입
result = [0] * (n+1)

while queue:
    now_Node = queue.popleft() # 큐에서 데이터 가져오기
    for next in cityList[now_Node]:
        indegree[next[0]] -= 1 # 진입차수 리스트 감소
        result[next[0]] = max(result[next[0]],result[now_Node] + next[1])
        # 경로 값이 더 큰 걸 선택하기, 기존 값과 경로가 추가된 것 중에서 큰거
        if indegree[next[0]] == 0:
            queue.append(next[0]) # 진입차수가 0이면 큐에 추가하기

resultCount = 0 # 1분도 쉬지 않고 달려야되는 도로 수
visited = [False] * (n+1) # 방문여부 표시
queue.clear()
queue.append(end)
visited[end] = True

# 위상정렬 역방향 수행
while queue:
    now = queue.popleft()
    for next in revcityList[now]:
        if result[next[0]] + next[1] == result[now]: 
            # 현재 노드에 영향을 준 이전 노드의 weight 생각
            resultCount += 1
            if not visited[next[0]]:
                visited[next[0]] = True
                queue.append(next[0])

print(result[end])
print(resultCount)