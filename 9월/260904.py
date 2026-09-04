def solution(n,costs):
    answer = 0
    costs.sort(key=lambda x: x[2]) # 0,1,2로 이루어진 배열 정렬
    parents = [i for i in range(n)]
    cnt = 0

    def find(x):
        if x == parents[x]:
            return x  # 부모노드 찾기
        
        parents[x] = find(parents[x])

        return parents[x]

    def union(x,y):
        rootx = find(x)
        rooty = find(y)

        if rootx == rooty:
            return

        if rootx < rooty:
            parents[rooty] = rootx
        else:
            parents[rootx] = rooty

    for start,end,cost in costs:
        if find(start)!= find(end):
            union(start,end)
            answer += cost
            cnt+= 1
        else:
            continue

        if cnt == n-1:
            break

    return answer