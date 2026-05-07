import sys
input = sys.stdin.readline

N = int(input()) #데이터 개수
A = list(map(int,input().split())) # 수 데이터 리스트 저장
A.sort() # 데이터 정렬
M = int(input()) # 탐색할 숫자 개수
target_list = list(map(int,input().split()))

for i in range(M):
    target = target_list[i]
    find = False

    # 이진 탐색 시작
    start = 0
    end = len(A) - 1
    while start <= end:
        midi = int((start + end) / 2)
        mid = A[midi]
        if mid >target:
            end = mid -1
        elif mid < target:
            start = mid + 1
        else:
            find = True
            break
    if find:
        print(1)
    else:
        print(0)
