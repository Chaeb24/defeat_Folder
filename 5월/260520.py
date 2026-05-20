N, M = map(int,input().split()) # N은 사람 수, M은 파티 수
trueP = list(map(int,input().split())) # 진실을 아는 사람 저장
T = trueP[0] # 진실을 아는 사람 수
del trueP[0]
result = 0
party = [[] for _ in range(M)] # 파티 수

def find(a): # 부모노드 찾기
    if parent[a] == a: # 자기자신과 숫자가 같으면 그대로 반환
        return a
    else:
        parent[a] = find(parent[a]) # 같지 않으면 재귀를 통해 루트 찾기
        return parent[a]
    
def union(a,b): # 각 노드의 부모 노드 찾는다.
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

for i in range(M):
    party[i] = list(map(int,input().split())) # 파티 데이터 저장
    del party[i][0] # 1번째, 2번째로 따지니까 첫번째 값 지우기

parent = [0] * (N+1)

for i in range(N+1): # 대표노드를 자신으로 초기화
    parent[i] = i 

for i in range(M): # 파티에 참여한 사람들 그룹으로 만들기
    firstPeople = party[i][0] # 그룹에 참여하면 루트노드 같아지니까 첫번째 사람만
    for j in range(1,len(party[i])):
        union(firstPeople,party[i][j])

for i in range(M):
    isPossible = True
    firstPeople = party[i][0]
    for j in range(len(trueP)): #진실을 아는 사람이 그룹에 있으면
        if find(firstPeople) == find(trueP[j]):
            isPossible = False
            break
    if isPossible: #진실을 아는 사람이 없으면
        # 카운트
        result += 1

print(result)