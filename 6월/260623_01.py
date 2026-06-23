N = int(input()) # 수 개수 저장
A = list(map(int,input().split())) # 수 데이터 리스트 저장
A.sort()
M = int(input()) # 탐색할 숫자 개수 저장
target_list = list(map(int,input().split()))

for i in range(M):
    find = False
    target = target_list[i] # 찾아야하는 수

    start = 0
    end = len(A) - 1
    while start <= end:
        midi = int((start + end) / 2)
        midv = A[midi]
        if midv > target:
            end = midi - 1
        elif midv < target:
            start = midi + 1
        else:
            find = True
            break
    if find:
        print(1)
    else:
        print(0)

