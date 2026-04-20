from itertools import combinations
# 1038 백준 
N = int(input())
result = []

for i in range(1, 11):
    for comb in combinations(range(10), i):
        num = int(''.join(map(str, comb[::-1])))
        result.append(num)

result.sort()

print(result[N] if N < len(result) else -1)