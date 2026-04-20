import sys
input = sys.stdin.readline

N, S, M = map(int,input().split()) # N은 노래 개수, S은 시작 볼륨, M은 최대볼륨
V = list(map(int,input().split())) # 볼륨 조절 정도
dp = [[False] * (M + 1) for _ in range(N + 1)] # 몇번째 곡에서 볼륨 조절 되는지 여부

dp[0][S] = True
# 시작점 설정
# 1495 백준 / DP 프로그래밍

for i in range(N):
    for j in range(M+1):
        if dp[i][j] == 1:
            min_val = j - V[i] # 최소 볼륨
            max_val = j + V[i] # 최대 볼륨
        
            if min_val >=0:
                dp[i+1][j - V[i]] = True # 다음 곡에 현재 볼륨 추가
            
            if max_val <= M :
                dp[i+1][j + V[i]] = True # 다음 곡에 현재 볼륨 추가

result = -1
# 최대 볼륨을 찾기 위함.
for i in range(M,-1,-1):
        if dp[N][i] == 1:
             result = i
             break
print(result)



        
