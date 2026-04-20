import math

t = int(input()) # 테스트케이스 수

# 9613 백준 문제

for _ in range(t):
    num_list = list(map(int,input().split()))
    sum = 0
    num = num_list[0] # 숫자 개수
    list_a = num_list[1:] # 계산해볼 숫자들

    # 리스트별로 확인
    for i in range(num):
        for j in range(i+1,num):
            a = math.gcd(list_a[i],list_a[j])
            sum += a
    print(sum)

