# 백준 1546

N = input()
mylist = list(map(int,input().split()))
mymax = max(mylist)

sum = sum(mylist)

print(sum * 100 / mymax / int(N))