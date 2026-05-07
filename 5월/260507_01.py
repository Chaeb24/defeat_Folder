N, M = map(int,input().split())
A = list(map(int,input().split()))
start = 0
end = 0

for i in A:
    if start < i:
        start = i  #레슨 최댓값을 시작 인덱스로
    end += i # 모든 레슨의 총합을 종료 인덱스로 저장

while start <= end:
    middle = int((start+end) / 2)
    sum = 0
    count = 0
    for i in range(N):
        if sum + A[i] > middle: # 블루레이 용량 초과
            count += 1 # 블루레이 개수 추가
            sum = 0 
        sum += A[i]
    if sum != 0: # 용량 초과 전, 체크
        count += 1
    if count > M:
        start = middle + 1
    else:
        end = middle - 1

print(start)


