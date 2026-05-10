import math

n = int(input())
result = n

for i in range(2,int(math.sqrt(result))+1):
    if n % i == 0: # 서로소이면
        result -= result / i
        while n % i == 0:
            n /= i # 같은 소인수를 중복 처리하지 않기 위함.

if n > 1:
    result -= result / n

print(int(result))