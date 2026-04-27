# 백준 11659
import sys

input = sys.stdin.readline

suNo, quizNo = map(int, input().split())

numbers = list(map(int, input().split()))

prefix_sum = [0]
temp = 0

for num in numbers:
    temp += num
    prefix_sum.append(temp)

for _ in range(quizNo):
    s, e = map(int, input().split())
    ans = prefix_sum[e] - prefix_sum[s - 1]
    print(ans)