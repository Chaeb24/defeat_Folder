# 백준 11659
import sys

input = sys.stdin.readline
suNo, quizNo = int(input().split())
# suNo는 숫자개수, quizNo는 질의 개수

numbers = list(map(int,input().split())) # 숫자 데이터 저장
prefix_sum = [0]
temp = 0

for num in numbers:
    temp = temp + num
    prefix_sum.append(temp)

for i in range(quizNo):
    s,e = int(input().split())
    ans = prefix_sum[e] - prefix_sum[s-1]
    print(ans)