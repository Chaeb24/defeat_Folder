import sys

input = sys.stdin.readline
S = input().strip()
T = input().strip()

# T를 S로 바꿔보는 생각
def dfs(T):

    if T == S:
        print(1)
        exit()
    
    if len(T)==0:
        return 0
    
    if T[-1] == 'A':
        if dfs(T[:-1]):
            return 1
    
    if T[0] == 'B':
        if dfs(T[1:][::-1]):
            return 1
    
    return 0

print(dfs(T))

