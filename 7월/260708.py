from collections import deque

def store(storage):
    N = len(storage)        
    M = len(storage[0])     
    
    
    grid = [["."] * (M + 2) for _ in range(N + 2)]

    for i in range(N):
        for j in range(M):
            grid[i + 1][j + 1] = storage[i][j]
    
    return grid

def fork(grid, target):
    R = len(grid)
    C = len(grid[0])

    visited = [[False] * C for _ in range(R)]

    # (0, 0) 출발선 설정
    queue = deque([(0, 0)])
    visited[0][0] = True 

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    to_delete = [] 

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
        
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:

                if grid[nr][nc] == ".":
                    visited[nr][nc] = True
                    queue.append((nr, nc))
                
                elif grid[nr][nc] == target: 
                    visited[nr][nc] = True
                    to_delete.append((nr, nc))
    
    for rr, cc in to_delete:
        grid[rr][cc] = '.'
        
    return grid

def crane(grid, target):
    R = len(grid)
    C = len(grid[0])

    for i in range(1, R - 1):
        for j in range(1, C - 1):
            if grid[i][j] == target:
                grid[i][j] = '.'
                
    return grid

def solution(storage, requests):
    grid = store(storage)
    
    for req in requests:
        target = req[0]
        if len(req) == 1:
            grid = fork(grid, target)
        elif len(req) == 2:
            grid = crane(grid, target)
            
    
    answer = 0
    R = len(grid)
    C = len(grid[0])
    
    for i in range(1, R - 1):
        for j in range(1, C - 1):
            if grid[i][j] != '.':
                answer += 1
                
    return answer