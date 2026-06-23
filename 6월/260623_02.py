N, M = map(int,input().split()) # N은 레슨 개수 / M은 블루레이 개수
A = list(map(int,input().split())) # 레슨 리스트
start = 0
end = 0

for i in A:
    if start < i:
        start = i # 레슨 최댓값을 시작 인덱스
    end += i # 모든 레슨의 총합을 종료 인덱스로 저장

while start <= end :
    middle = int((start + end) / 2)
    sum = 0
    count = 0
    for i in range(N):
        if sum + A[i] > middle:
            count += 1
            sum = 0 # 현재 블루레이에서 새 블루레이로 교체, sum은 초기화
        sum += A[i]
    if sum != 0: # 남은 블루레이가 0이 아니고 레슨이 남아있다면
        count += 1
    if count > M:
        start = middle + 1
    else:
        end = middle - 1

print(start)

