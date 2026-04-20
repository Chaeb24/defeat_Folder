# 4659번
N, M = map(int, input().split()) # 듣지도 못한 사람, 보지도 못한 사람

not_heard = set()
not_seen = set()
NM = [] # 교집합 찾아서 추가하기

for _ in range(N):
    not_heard.add(input()) # 이름값 입력받기

for _ in range(M):
    not_seen.add(input())

for name in not_heard:
    if name in not_seen:
        NM.append(name)

NM.sort()
print(len(NM))
print(NM)
        



