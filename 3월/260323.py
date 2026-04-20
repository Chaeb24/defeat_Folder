import sys

input = sys.stdin.readline
tc = int(input())

# 3085 문제

colors = [list(input().strip()) for _ in range(tc)]
ans = 0

def check():
    max_cnt = 1 
    # 가로 확인
    for i in range(tc):
        cnt = 1
        for j in range(1,tc):
            if colors[i][j] == colors[i][j-1]: # 행을 고정 시킴.
                cnt +=1
                max_cnt = max(cnt, max_cnt)
            else:
                cnt = 1
            
    # 세로 확인
    for j in range(tc):
        cnt = 1
        for i in range(1,tc):
            if colors[i][j] == colors[i - 1][j]: # 열을 고정시킨 후 행끼리만 비교
                cnt += 1
                max_cnt = max(cnt, max_cnt)
            else:
                cnt = 1
            
    return max_cnt

for i in range(tc):
    for j in range(tc-1):
        # 가로 교체
        colors[i][j],colors[i][j+1] = colors[i][j+1], colors[i][j]
        ans = max(ans,check())
        colors[i][j+1],colors[i][j] = colors[i][j],colors[i][j+1]

        # 세로 교체
        colors[j][i],colors[j+1][i] = colors[j+1][i],colors[j][i]
        ans = max(ans,check())
        colors[j+1][i],colors[j][i] = colors[j][i],colors[j+1][i]

print(ans)

    
