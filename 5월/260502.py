# 백준 15649

n,m = int(input().split())
visited = [False] * n
S= [0] * m

def backtrack(length):
    if length == m:
        print(' '.join(str(x+1) for x in S))
        return
    
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            S[length] = i
            backtrack(length+1)
            visited[i] = False

backtrack(0)