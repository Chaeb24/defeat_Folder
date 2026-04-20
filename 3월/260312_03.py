import sys
input = sys.stdin.readline
# 백준 2304 창고 다각형

m = 0 # 높이 표시하기 위한 인덱스 
m_idx = 0 # 지점 표시하기 위한 인덱스
pli = [0 for _ in range(1001)] # 기둥
for _ in range(int(input())):
    L,H = map(int,input().split()) # 위치, 높이.
    pli[L] = H
    if m < H: # 가장 높은 기둥과 그 기둥의 인덱스를 찾음
        m_idx = L
        m = H
curr = 0
answer = 0
for i in range(m_idx+1): # 왼쪽 그룹
    curr = max(curr,pli[i])
    answer += curr
curr = 0
for i in range(1000,m_idx,-1): # 오른쪽 그룹
    curr = max(curr,pli[i])
    answer += curr
print(answer)