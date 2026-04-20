import sys

# 14719 백준

input = sys.stdin.readline
H, W = map(int,input().split())
# H가 가로 W가 세로

pipe = list(map(int,input().split()))
water = 0

for i in range(1,W-1):
    left_max = max(pipe[:i])
    right_max = max(pipe[i+1:])

    height = min(left_max,right_max)

    if pipe[i] < height:
        water += (height-pipe[i])

print(water)

