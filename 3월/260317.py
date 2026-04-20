# 7568 백준

N = int(input()) # 몇 명의 사람이 있는가
info = []

for _ in range(N):
    weight,height = map(int,input().split())
    info.append((weight,height)) # 몸무게랑 키


for i in info:
    rank = 1

    for j in info:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end = ' ')