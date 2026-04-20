import sys

input = sys.stdin.readline
# 백준 1806
N, S = map(int,input().split()) # N은 숫자 개수, S는 합
arr = list(map(int, input().split()))

left,right = 0,0
sum = 0
min_length = 1e9

while True:
    if sum >= S:
        min_length = min(min_length,right-left)
        sum -= arr[left]
        left += 1
    elif right == N:
        break
    else:
        sum += arr[right]
        right +=1

if min_length == 1e9:
    print(0)
else:
    print(min_length)