import sys
input = sys.stdin.readline

# 백준 20207, 일정 계산 문제

n = int(input())
arr = [0] * 366
ans = 0

for i in range(n):
    start, end = map(int, input().split())
    while start <= end:
        arr[start] +=1 # 일정 길이만큼 테이프로 붙이기
        start +=1

rows, cols = 0,0

for i in range(366):
    if arr[i] == 0: # 일정이 비는 날을 만났을 때
        ans += rows * cols # 테이프 붙인 넓이 구하기
        rows, cols = 0,0
        continue

    rows += 1 # 연속된 날짜수 가로로 증가
    cols=max(cols, arr[i]) # 세로 중에 가장 많이 겹친 날

print(ans + rows*cols)