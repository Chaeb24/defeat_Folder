# 백준 3474

T = int(input()) #테스트 케이스

for _ in range(T):
    N = int(input()) # 몫이 될 수
    total = 0

    while N > 0:
        N = N // 5
        total += N
    print(total)
    
