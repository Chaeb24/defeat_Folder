import sys

input = sys.stdin.readline

N = int(input()) # 숫자 몇개
num = list(map(int,input().split())) # 숫자 배열
plus,minus,mul,div = map(int, input().split())
answer = []

def dfs(plus,minus,mul,div,res=0,i=0):

    if plus == 0 and minus == 0 and mul == 0 and div == 0: #모든 연산자 순회가 끝남.
        answer.append(res)
        return

    # 재귀처리
    if plus:
        dfs(plus-1,minus,mul,div,res+num[i],i+1)
    
    if minus:
        dfs(plus,minus-1,mul,div, res-num[i],i+1)
    
    if mul:
        dfs(plus,minus,mul-1,div, res*num[i],i+1)
    
    if div:
        if res > 0:
            dfs(plus,minus,mul,div-1, int(res/num[i]),i+1)
        else:
            dfs(plus,minus,mul,div-1, -int(-res/num[i]),i+1)

dfs(plus,minus,mul,div,num[0],1) # total 초기값은 nums[0]
print(max(answer))
print(min(answer))