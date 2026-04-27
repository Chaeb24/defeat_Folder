import sys
input = sys.stdin.readline
N = int(input()) # 수의 개수
A = list(map(int,input().split()))
result = 0
tmp = [0] * int(N+1)
# 백준 1517 버블정렬

def merge_sort(s,e):
    global result
    if e-s < 1: return
    m = int(s + (e-s)/2)
    merge_sort(s,m)
    merge_sort(m+1,e)
    for i in range(s, e+1):
        tmp[i] = A[i]
    k = s
    index1 = s
    index2 = m + 1
    while index1 <= m and index2 <= e:
        if tmp[index1] > tmp[index2]:
            A[k] = tmp[index2]
            result = result + index2 - k
            k += 1
            index2 += 1
        else:
            A[k] = tmp[index1]
            k += 1
            index1 += 1
    while index1 <= m:
        A[k] = tmp[index1]
        k += 1
        index1 += 1
    while index2 <= e:
        A[k] = tmp[index2]
        k += 1
        index2 += 1

A.insert(0,0)
merge_sort(1,N)
print(result)



