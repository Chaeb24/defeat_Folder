from collections import deque

def solution(m,n,h,w,drops):
    answer = []
    INF = len(drops) + 1 # drops 는 빗방울 떨어지는 위치

    time = [[INF] * n for _ in range(m)]
    for i in range(len(drops)):
        a,b = drops[i]
        time[a][b] = i+1 # 빗방울 떨어지는 순서 저장
    
    width = n-w +1 # 슬라이딩 윈도우 경우의 수
    row_min = [[0] * width for _ in range(m)]

    for i in range(m):
        dq = deque()
        for j in range(n):
            while dq and time[i][dq[-1]] >= time[i][j]:
                # 앞에 있는 숫자가 슬라이딩 윈도우로 사라지게 되고 어차피 최솟값 아님
                dq.pop()
            dq.append(j)

            # 슬라이드 범위 밖 제거
            while dq and dq[0] <= j-w:
                dq.popleft()
            
            if j >= w-1:
                row_min[i][j-w+1] = time[i][dq[0]] # 행을 기준으로 삼고 최솟값을 찾기
            
        
    height = m-h+1
    rect_min = [[0] * width for _ in range(height)]
    for j in range(width):
        dq = deque()
        for i in range(m): # 열을 기준으로 삼고 최솟값 찾기
            while dq and row_min[dq[-1]][j] >= row_min[i][j]:
                dq.pop()
            dq.append(i)

            while dq and dq[0] <= i-h:
                dq.popleft()
            
            if i >= h-1:
                rect_min[i-h+1][j] = row_min[dq[0]][j]
    

    maxValue = -1
    answer = [0,0]

    for i in range(height):
        for j in range(width):
            if rect_min[i][j] > maxValue:
                maxValue = rect_min[i][j]
                answer = [i, j]
            
    return answer