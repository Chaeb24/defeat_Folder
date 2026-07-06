import heapq

def solution(N, road, K):
    answer = 0

    INF = int(1e9)

    
    distance = INF * (N+1) # 거리 리스트
    graph = [[] for _ in range(N+1)] #데이터 저장 인접 리스트

    for r in road:
        graph[r[0]].append((r[1], r[2]))
        graph[r[1]].append((r[0], r[2]))
    
    queue = []
    start = 1

    heapq.heappush(queue,(0,start))
    distance[start] = 0 # 거리 리스트 초기화

    while queue:
        dist, now = heapq.heappop(queue) #연결된 다음 노드
        if distance[now] < dist: #이미 업데이트 된 거리라면
            continue
        else:
            for i in graph[now]:
                cost = dist + i[1] # 거리 업데이트
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(queue,(cost,i[0])) #거리, 다음 노드
    
    for i in distance:
        if i < K: # 정해진 시간보다 적으면
            answer += 1

    return answer