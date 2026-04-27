import sys
# 백준 1253 좋은 수
input = sys.stdin.readline
N = int(input()) # 수의 개수
A = list(map(int,input().split()))
A.sort() 
result = 0

for k in range(N):
    find = A[k]
    i = 0
    j = N -1
    while i<j:
        if A[i] + A[j] == find:
            if i != k and j != k:
                result += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1
        elif A[i] + A[j] < find:
            i += 1
        else:
            j -= 1

print(result)