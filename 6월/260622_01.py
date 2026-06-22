from collections import queue

# 슬라이딩 윈도우
# 최소값 가능성 없으면 삭제해도 상관없음
# 윈도우 범위 벗어나면 삭제
N,L = map(int,input().split())
mydeque = queue()
now = list(map(int,input().split()))

for i in range(N):
    while mydeque and mydeque[-1][0] > now[i]:
        # 방금 입력받은 값보다 덱 앞에 있는 값이 크다면
        mydeque.pop()
    mydeque.append((now[i],i)) # 값, 인덱스
    if mydeque[0][1] <= i-L:
        # 범위를 벗어났다면
        mydeque.popleft()
    print(mydeque[0][0],end=' ')