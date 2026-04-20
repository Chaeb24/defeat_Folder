import sys
import heapq  # 백준 11286

input = sys.stdin.readline
N = int(input())
heap = []

for _ in range(N):
    X = int(input().strip())

    if X:
        heapq.heappush(heap,(abs(X),X)) # 튜플 형식으로 삽입
    else:
        if heap:
            print(heapq.heappop(heap[1]))
        else:
            print(0)