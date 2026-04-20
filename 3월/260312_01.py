import sys
import heapq

# 11279 짝꿍 문제, 1927번
input = sys.stdin.readline
N = int(input()) #테스트 케이스 개수
heap = [] # 최소 힙 결과 뽑기전
min_heap = [] # 결과 값만

for _ in range(N):
    X = int(input())

    if X > 0 : # 자연수 이면
        heapq.heappush(heap,X) # heap에 추가
    elif X == 0: # 입력값이 0이면
        if heap:
            a = heapq.heappop(heap) # 최솟값 뽑기
            min_heap.append(a)
        else:
            min_heap.append(0)

for i in range(len(min_heap)):
    print(min_heap[i])