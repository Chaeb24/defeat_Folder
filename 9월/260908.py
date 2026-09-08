def solution(board, h, w):
    
    n = len(board) # 일단 세로길이 저장
    count = 0 # 같은 색깔인 칸의 개수 저장용

    dh = [0, 1, -1, 0]
    dw = [1, 0, 0, -1]

    # 순회하면서 같은 색깔이 있는지 체크
    for i in range(4):
        h_check = h + dh[i]
        w_check = w + dw[i]
        if n> h_check >=0 and n> w_check >=0 and board[h][w] == board[h_check][w_check]:
            count += 1

    return count