A,B,C = map(int,input().split())

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

def execute(a,b):
    ret = [0] * 2
    if b == 0:
        ret[0] = 1
        ret[1] = 0
        return ret
    q = a // b
    v = execute(b,a%b) # 재귀형태로 유클리드 호제법 실행
    ret[0] = v[1] # x값에 이전 y값 대입
    ret[1] = v[0] - v[1] * q # y값에 이전 x값 대입
    return ret 

mgcd = gcd(A,B)

if C % mgcd != 0:
    print(-1)
else:
    mok = int(C / mgcd)
    ret = execute(A,B)
    print(ret[0] * mok, end = ' ')
    print(ret[1] * mok)


