
def gcd(a,b):
    if b == 0:
        return a
    
    else:
        return gcd(b,a%b)
    
T = int(input()) # 테스트 케이스

for i in range(T):
    A,B = map(int,input().split())
    result = A * B / gcd(A,B)
    print(int(result))