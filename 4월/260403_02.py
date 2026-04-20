import sys
input = sys.stdin.readline
N,X = map(int,input().split()) # 날짜

visitors = list(map(int,input().split())) # 방문자 수


value = sum(visitors[:X])
max_value = value
cnt = 1

for i in range(X,N):
    value += visitors[i]
    value -= visitors[i-X]

    if value > max_value:
        max_value = value
        cnt = 1
    elif value == max_value:
        cnt += 1

if max_value>0:
    print(max_value)
    print(cnt)
else:
    print("SAD")
        
