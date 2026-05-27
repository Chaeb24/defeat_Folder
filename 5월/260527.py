def fork(storage,box):
    dx = [0,0,-1,1]
    dy = [1,-1,0,0]
    index = [] # 위치 저장용

    for i in range(1,len(storage)-1): # 세로 기준
        for j in range(1,len(storage[0])-1): # 가로 기준
            if storage[i][j] == box : # 박스 위치랑 같으면
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if storage[nx][ny] == "0" # 지게차 접근 가능 표시
                        index.append((i,j))
                        break
    
    for i, j in index:
        storage[i][j] = "0"
        isOutside(storage,i,j) #주변에 빈공간 있으면 외부랑 연결

def crane(storage,box):
    for i in range(1,len(storage)-1):
        for j in range(1,len(storage[0])-1):
            if storage[i][j] == box:
                storage[i][j] = "1" # 크레인으로 꺼내기 가능 표시
                isOutside(storage,i,j)

def isOutside(storage,x,y):
    dx,dy = [0,0,-1,1][1,-1,0,0]
    outside = False

    for i in range(4):
        nx,ny = x + dx[i], y + dy[i]
        if storage[nx][ny] == "0":
            storage[x][y] = "0"
            outside = True
            break
    
    if outside:
        for i in range(4):
            nx,ny = x + dx[i], y + dy[i]
            if storage[nx][ny] == "1":
                storage[nx][ny] = "0"
                isOutside(storage,nx,ny)

def solution(storage,requests):
    answer = 0
    storage = [list("0" + i + "0") for i in storage] # 테두리를 "0"으로 채움
    storage.insert(0,list("0" * len(storage[0]))) # 위에 0번 인덱스부터
    storage.append(list("0" * len(storage[0]))) # 아래를 0으로 패딩

    for q in requests:
        if len(q) == 1: # 길이가 하나인 박스 찾기
            fork(storage,q)
        else:
            crane(storage,q[0])
    
    for i in range(1, len(storage)-1):
        for j in range(1, len(storage[0])-1):
            if storage[i][j] not in ["0", "1"]:
                answer += 1
    
    return answer
        