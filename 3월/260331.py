import sys
input = sys.stdin.readline

n = int(input())
cnt = 0
# 백준 14916
while n >= 0:
    if n % 5 == 0:
        print(cnt + n // 5)
        break
    n -= 2
    cnt += 1
else:
    print(-1)