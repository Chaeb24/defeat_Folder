import sys
from collections import Counter

# 9017번 백준
input = sys.stdin.readline
T = int(input())

for _ in range(T):
    N = int(input())
    teams = list(map(int,input().split()))
    counter = Counter(teams) # 팀이 몇번 나왔는지 세는 기능
    scores = {}

    rank = 1
    for i in range(N):
        if counter[teams[i]] == 6:
            if teams[i] in scores:
                scores[teams[i]].append(rank)
            else: # 카운터 라이브러리에 팀이 없으면 새로 등록
                scores[teams[i]] = [rank]
            rank += 1
    
    print(sorted(scores, key = lambda x:(sum(scores[x][0:4]), scores[x][4]))[0])






    

