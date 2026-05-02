# 색종이 붙이기
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

# 종이 데이터
M = [list(map(int,input().split())) for _ in range(10)]

S = [0, 5, 5, 5, 5, 5]
result = float('inf')

def fill(x,y,size,value):
    for i in range(y,y+size):
        for j in range(x,x+size):
            M[i][j] = value

def check(x,y,size):
    if x + size > 10 or y + size > 10:
        return False
    for i in range(y,y+size):
        for j in range(x, x+size):
            if M[i][j] != 1:
                return False
    return True 

def backtrack(pos,used):
    global result
    if pos == 100:
        result = min(result,used)
        return
    if used >= result:
        return
    x, y = divmod(pos,10) # 나눗셈 몫과 나머지
    if M[y][x] == 1:
        for size in range(5,0,-1):
            if S[size] > 0 and check(x,y,size): # 색종이 여분이 있고, 덮어야되는 부분이라면
                S[size] -= 1 # 색종이 사용하고
                fill(x,y,size,0) # 채우기
                backtrack(pos+1, used+1)
                fill(x,y,size,1) # 다시 돌아오기
                S[size] += 1
            else:
                backtrack(pos + 1, used)

backtrack(0,0)
print(result if result != float('inf') else -1)