import sys

K,N = map(int,sys.stdin.readline().split())
arr = [int(sys.stdin.readline()) for _ in range(K)]

# 길이 범위
start = 1
end = max(arr) # 랜선 최대 길이

while start <= end:
    mid = (start+end)//2
    count = 0
    
    for x in arr:
        count += x // mid
    
    # N개의 개수보다 많으면 더 큰 값으로 기준을 설정
    if count >= N:
        start = mid + 1
    else:
        end = mid -1

print(end)
