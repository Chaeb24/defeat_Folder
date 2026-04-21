import sys

input = sys.stdin.readline
N = int(input()) # 재료의 개수
M = int(input()) # 갑옷이 되는 번호합
A = list(map(int,input().split()))
A.sort() # A 오름차순 정렬
# 인덱스 설정
i = 0
j = N-1
count = 0

while i<j:
    if A[i] + A[j] < M:
        i += 1
    elif A[i] + A[j] > M:
        j -= 1
    else:
        count += 1
        i += 1
        j -= 1

print(count)