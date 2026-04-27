N = int(input()) # 데이터 개수
A = list(map(int,input().split())) # 돈 인출하는데 필요한 시간
S = [0] * N # 합 배열
# 백준 11399
for i in range(1, N):
    point = i
    time = A[i] # 기준
    for j in range(i-1,-1,-1):
        if A[j] < A[i]:
            point = j + 1
            break
        if j == 0:
            point = 0
    for j in range(i,point,-1):
        A[j] = A[j-1]
    A[point] = time

S[0] = A[0]

for i in range(1,N):
    S[i] = S[i-1] + A[i] # 합 배열 만들기

sum = 0

for i in range(0,N):
    sum += S[i]

print(sum)