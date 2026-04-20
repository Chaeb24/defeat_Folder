# 2504

stack = []

N = input().strip()
result = 0
temp = 1

for i in range(len(N)):
    if N[i] == '(':
        temp *= 2
        stack.append('(')
    
    elif N[i] == '[':
        temp *= 3
        stack.append('[')
    
    elif N[i] == ')': # )를 만났는데
        if not stack or stack[-1] != '(':  # 스택이 비어있거나 (로 시작이 안 된거면
            result = 0
            break
        if N[i-1] == '(': 
            result += temp

        stack.pop()
        temp //=2  # ()로 끝난거니까 원상복귀 
    
    elif N[i] == ']': # ]를 만났는데
        if not stack or stack[-1] != '[':
            result = 0
            break
        if N[i-1] == '[':
            result += temp
        
        stack.pop()
        temp //=3

if stack:
    print(0)
else:
    print(result)
    