answer = 0
A = list(map(str,input().split('-')))  # "-" 기호를 기준으로 split진행

def mySum(i):
    ch = str(i).split('+')
    sum = 0

    for c in ch:
        sum += int(c)
    
    return sum

for i in range(len(A)):
    res = mySum(A[i])
    if i == 0: # 첫번째 그룹인가
        answer += res
    else:
        answer -= res

print(answer)

