# 백준 11720

n = input() # 숫자 몇개
numbers = list(input())
# numbers 변수에 list 함수 이용하여 숫자를 한 자리씩 나누어 받기
sum = 0 # sum 변수 선언

for num in numbers:
    sum = sum + int(num)

print(sum)