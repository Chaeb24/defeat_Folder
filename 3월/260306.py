import sys

# 2512번 문제
n = int(sys.stdin.readline())
organ = list(map(int, sys.stdin.readline().split())) # 각 지방에서 예산 요청한 금액
m = int(sys.stdin.readline()) # 총 예산 한도

start, end = 0, max(organ)
while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in organ:
        total += min(mid, i)
    # 상한선 설정하기 위한 로직

    if total > m:
        end = mid - 1
    else:
        start = mid + 1
print(end)