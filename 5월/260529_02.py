from collections import deque

N = int(input()) # 건물 종류 수 입력받기
A = [[] for _ in range(N+1)] # 건물 데이터 저장 리스트
selfBuild = [0] * (N+1)
indegree = [0] * (N+1) # 진입차수 리스트

# N번만큼 입력받은거 기록
for i in range(1,N+1):
    inputList = list(map(int,input().split()))
    selfBuild[i] = (inputList[0]) # 해당 건물을 짓는데 걸리는 시간
    index = 1
    while True:
        preTemp = inputList[index]
        index += 1
        if preTemp == -1 : #끝이라는 의미
            break
        A[preTemp].append(i)
        indegree[i] += 1 #진입차수 데이터 저장
    
queue = deque()

for i in range(1,N+1):
    if indegree[i] == 0: # 진입차수가 0인거 먼저 시작함.
        queue.append(i)

result = [0] * (N+1)

while queue:
    now = queue.popleft()
    for next in A[now]:
        indegree[next]-=1 # 시간을 업데이트 시켜줌.
        result[next] = max(result[next],result[now] + selfBuild[now])
        if indegree[next] == 0:
            queue.append(next)

for i in range(1,N+1):
    print(result[i] + selfBuild[i])

