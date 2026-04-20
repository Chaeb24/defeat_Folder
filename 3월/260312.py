# 11279번 백준
import heapq
import sys

input = sys.stdin.readline
N = int(input()) # 테스트 케이스 수 입력 받기
heap = [] # 최대 힙 만들기 전 사용하는 리스트
max_heap = [] # 결과값만 나오게 하기


for _ in range(N):
    X = int(input())

    if X > 0 : # X가 자연수야
        heapq.heappush(heap,-X) # 힙에 X를 추가해
    elif X == 0: # X가 0이면
        if heap:
            a = -heapq.heappop(heap)
            max_heap.append(a) 
        # 힙에서 최대값을 빼서 결과값 리스트에만 넣어주면 됨.
        else:
            max_heap.append(0)

for i in range(len(max_heap)):
    print(max_heap[i])
