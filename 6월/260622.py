checkList = [0] * 4 # 비밀번호 체크 리스트
myList = [0] * 4 # 현재리스트
checkSecret = 0 

def myadd(c):
    global checkList,myList,checkSecret
    if c == 'A':
        myList[0] += 1
        if myList[0] == checkList[0]:
            checkSecret += 1
    elif c == 'C':
        myList[1] += 1
        if myList[1] == checkList[1]:
            checkSecret += 1
    elif c == 'G':
        myList[2] += 1
        if myList[2] == checkList[2]:
            checkSecret += 1
    elif c == 'T':
        myList[3] += 1
        if myList[3] == checkList[3]:
            checkSecret += 1

def myremove(c):
    global checkList,myList,checkSecret
    if c == 'A':
        if myList[0] == checkList[0]:
            checkSecret -= 1
        myList[0] -= 1
    elif c == 'C':
        if myList[1] == checkList[1]:
            checkSecret -= 1
        myList[1] -= 1
    elif c == 'G':
        if myList[2] == checkList[2]:
            checkSecret -= 1
        myList[2] -=1
    elif c == 'T':
        if myList[3] == checkList[3]:
            checkSecret -= 1
        myList[3] -= 1

S,P = map(int,input().split()) # DNA 문자열, 부분문자열(슬라이딩용)
Result = 0
A = list(input())
checkList = list(map(int,input().split()))

for i in range(4): # 이미 조건을 만족했다면 경우의 수 세기
    if checkList[i] == 0:
        checkSecret += 1

for i in range(P): 
    myadd(A[i])
if checkSecret == 4: # A,C,G,T 조건이 모두 만족되면 경우의 수 세기
    Result += 1

for i in range(P,S):
    j = i - P # 제외될 문자 인덱스
    myadd(A[i]) # 새롭게 들어오는 문자(맨 오른쪽) 추가
    myremove(A[j]) # 제외되는 문자인덱스 빼주기
    if checkSecret == 4:
        Result += 1

print(Result)