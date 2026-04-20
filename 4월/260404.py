import sys
input = sys.stdin.readline

def solution():
    N, M, K = map(int, input().split())

    # 배열 초기화 (-1로)
    board = [[-1] * M for _ in range(N)]

    # 방향: 오른쪽 → 아래 → 왼쪽 → 위
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]

    x, y = 0, 0   # 시작 위치
    d = 0         # 방향 인덱스

    for num in range(1, K + 1):
        board[y][x] = num

        nx = x + dx[d]
        ny = y + dy[d]

        # 범위를 벗어나거나 이미 채운 칸이면 방향 변경
        if not (0 <= nx < M and 0 <= ny < N) or board[ny][nx] != -1:
            d = (d + 1) % 4
            nx = x + dx[d]
            ny = y + dy[d]

        x, y = nx, ny

    # 출력
    for row in board:
        print(*row)


solution()