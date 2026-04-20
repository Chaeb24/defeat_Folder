# 1874번

N = int(input())

stack = []
result = [] # POP한 결과 저장하는 리스트
next_num = 1 # 다음에 어떤 숫자 들어갈지 기록용
temp = True

for i in range(N):

    num = int(input()) # 숫자 입력

    # 첫번째 값만큼 push
    
    while next_num <= num:
        stack.append(next_num)
        result.append("+")
        next_num += 1

    if stack[-1] == num:
        a = stack.pop()
        result.append("-")
    else:
        temp = False
        break

if temp:
    for i in result:
        print(i)
else:
    print("NO")
   

