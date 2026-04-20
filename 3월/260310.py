# 3986번
N = int(input()) # 개수

count = 0

for _ in range(N):

    word = input()
    stack = [] 
    # 함수안에 넣는 이유는 매번 새로운 단어 확인해야되기 때문에

    for w in word: # 같은 단어이면 pop, 아니면 push
        if stack and stack[-1] == w: # 스택이 비어있지 않고, 스택의 마지막 요소가 현재 단어와 같으면
            stack.pop()
        else:
            stack.append(w)
    
    # 하나의 단어 검사 후 스택이 비었는지만 검사
    if not stack:
        count += 1
        
        
print(count)
