# 20920번 - 영단어 암기는 괴로워
import sys
input = sys.stdin.readline
N, M = map(int, input().split()) # 단어 개수, 외울 단어 길이 기준

# 자주 나오는 단어인가
words_count = {}

for _ in range(N):
    word = input().strip()
    
    count = 0

    if len(word) < M:
        continue
    else: 
        if word in words_count: #이미 나온 단어
            words_count[word] += 1
        else:
            words_count[word] = 1


# 단어, 단어 빈도로 딕셔너리에 저장됨.
# 단어 빈도가 많이 나오는 순 / 단어 길이가 긴 순서대로 / 그 다음 알파벳 순서대로 정렬
d = sorted(words_count.items(), key=lambda x:(-x[1], -len(x[0]), x[0]))

for i in d:
    print(i[0])
