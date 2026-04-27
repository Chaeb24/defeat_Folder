import sys
input = sys.stdin.readline
# 백준 1377 버블정렬
N = int(input()) # 데이터 개수
A = []

for i in range(N):
   A.append((int(input()), i)) # 인덱스 비교를 위해 튜플로 저장

Max = 0
sorted_A = sorted(A) # 리스트 정렬

for i in range(N):
    if Max < sorted_A[i][1] - i:
        Max = sorted_A[i][1] -i

print(Max+1) # swap 필요없는지 여부 체크 한번 더