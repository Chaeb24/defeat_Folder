# 1916 백준
import sys
import heapq
input = sys.stdin.readline

INF = int(1e9) # 무한대로 설정

N = int(input()) # 도시 수
M = int(input()) # 버스 수
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1) # 거리는 무한대

for _ in range(M):
    sv,ev,cost = map(int,input().split()) # 도시와 도시 사이 이동 비용
    graph[sv].append((ev,cost))

start, end = map(int,input().split()) # 시작점과 끝 점 입력


def dijkstra(start):

    heap = []
    distance[start] = 0 # 시작점 초기화
    heapq.heappush(heap,[distance[start],start])

    while heap:
        curCost,curNode = heapq.heappop(heap)

        if distance[curNode] < curCost:
                continue
        
        # 목적지면 종료 가능
        if curNode == end:
            break

        for i in graph[curNode]:
            cost = curCost + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))


dijkstra(start)

print(distance[end])


