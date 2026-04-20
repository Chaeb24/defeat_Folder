import sys
import heapq

# 2075번: N번째 큰 수

input = sys.stdin.readline
N = int(input()) # 표 몇 칸으로 만들지 정하기

arr = []
for i in range(N):
    nums = list(map(int,input().split()))

    for row in nums:
        if len(arr) < N : # 일정 칸보다 입력 값이 작으면
            heapq.heappush(arr,row)
        else: # 입력 값이 다 찼어
            if arr[0] < row: # 가장 작은 값인지 확인
                heapq.heappushpop(arr, row)
print(arr[0])

