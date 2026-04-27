import sys
from collections import deque
input = sys.stdin.readline
# 백준 11003 최솟값 찾기 -> 골드1로 강등됨.
N, L = map(int,input().split())
mydeque = deque()
now = list(map(int,input().split()))

for i in range(N):
    # 나보다 큰 데이터 삭제하기
    while mydeque and mydeque[-1][0] > now[i]:
        mydeque.pop()
    mydeque.append((now[i],i))
    if mydeque[0][1] <= i - L:
        mydeque.popleft()
    print(mydeque[0][0],end= ' ')