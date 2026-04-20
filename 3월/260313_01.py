import sys

input = sys.stdin.readline
H, W = map(int,input().split())

# 10709번 백준
for _ in range(H):
    row = input().strip()
    result = []
    cloud = -1 # 구름이 없는 상태는 -1로 표현

    for ch in row:
        if ch == 'c': # 구름이 있는 경우
            cloud = 0
            result.append(0)
        else:
            if cloud == -1:
                result.append(-1)
            else: # 구름이 있는 상태에서 구름이 없는 칸이 나오면 구름의 거리를 1씩 증가
                cloud += 1
                result.append(cloud)
    print(*result)



