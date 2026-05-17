import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

N, M = map(int,input().split()) #원소, 질의개수
parent = [0] * (N+1)

def find(a):
    if parent[a] == a:
        return a
    else:
        parent[a] = find(parent[a]) # 대표노드가 같을때까지 찾기
        return parent[a]

def union(a,b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

def checkSame(a,b):
    num1 = find(a)
    num2 = find(b)
    if num1 == num2:
        return True
    else:
        return False

for i in range(0,N+1):
    parent[i] = i # 대표노드 자기자신으로 초기화

for i in range(M):
    question,a,b = map(int,input().split())
    if question == 0:
        union(a,b)
    else:
        if checkSame(a,b):
            print("YES")
        else:
            print("NO")


