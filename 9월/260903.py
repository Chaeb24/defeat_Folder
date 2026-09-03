from collections import deque

def solution(maps):
    n, m = len(maps[0]), len(maps)
    visited = [[False] * n for _ in range(m)]
    visited[0][0] = True

    delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q = deque([])
    q.append((1, 0, 0))

    while q:
        cnt, y, x = q.popleft()

        if x == n-1 and y == m-1:
            return cnt

        for dy, dx in delta:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and visited[ny][nx] == False and maps[ny][nx] == 1:
                q.append((cnt+1, ny, nx))
                visited[ny][nx] = True

    return -1



