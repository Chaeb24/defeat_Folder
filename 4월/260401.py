import sys

input = sys.stdin.readline
# 백준 11047 그리디
N, K = map(int,input().split())
# N은 동전 개수, K는 합
arr = [int(input()) for _ in range(N)]

cnt = 0

for i in range(N-1,-1,-1):
    cnt += K // arr[i]
    K %= arr[i]

print(cnt)
        