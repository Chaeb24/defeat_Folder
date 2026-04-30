import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
N = int(input())
# 백준 2023 탐색

def isPrime(num):
    for i in range(2,int(num / 2 + 1)):
        if num % i == 0: # 1과 자신 외에 나눠지면
            return False
    return True

def DFS(number):
    if len(str(number)) == N: # 자릿수가 같은지 여부
        print(number)
    else:
        for i in range(1,10):
            if i % 2 == 0: # 짝수면 제외
                continue
            if isPrime(number * 10 + i):
                DFS(number*10 + i)

DFS(2)
DFS(3)
DFS(5)
DFS(7)