# 오큰수 구하기
import sys
N = int(input()) # 수열의 크기
A = list(map(int,input().split())) # A리스트 입력 받기

stack = []
ans = [0] * N # 결과값 저장

for i in range(N):
    while stack and A[stack[-1]] < A[i]: # 스택의 맨 위
        ans[stack.pop()] = A[i] # 값이 크면 오큰수에 해당됨.
        stack.append(i) # 인덱스 스택에 추가

while stack:
    ans[stack.pop()] = -1

for i in range(N):
    sys.stdout.write(str(ans[i]) + " ")