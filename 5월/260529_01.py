from collections import deque # BFS 실행을 위한 세팅

def solution(land):
    answer = 0 # 반환을 위한 값
    n,m = len(land),len(land[0]) # n은 세로, m은 가로 설정

    # BFS 이동방향
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]

    # 각 열의 기름총량
    result = [0 for _ in range(m)]
    # 방문기록
    visited = [[0 for _ in range(m)] for _ in range(n)]

    def bfs(pos):
        a,b = pos # land의 좌표찍기
        cnt = 1
        visited[a][b] = 1 #방문표시하기

        q = deque()
        q.append(pos) # 큐에 추가해주기

        # 석유 존재하는 열 저장
        oil_covered = set()
        oil_covered.add(b)

        while q:
            x,y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i] # 상하좌우로 이동하면서 찾다가 방문 안하고 석유는 있을 때
                if (0 <= nx < n) and (0 <= ny < m) and visited[nx][ny] == 0 and land[nx][ny] == 1:
                    q.append((nx,ny))
                    visited[nx][ny] = 1
                    cnt += 1
                    oil_covered.add(ny) # 열만 저장

        for c in oil_covered:
            result[c] += cnt

    for i in range(n):
        for j in range(m):
            if (land[i][j] == 1) and not visited[i][j]:
                bfs((i, j))
    
    answer = max(result)
    
    return answer