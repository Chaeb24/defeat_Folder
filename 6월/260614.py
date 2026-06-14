def solution(n, infection, edges, k):
    # 그래프 구성
    graph = [[] for _ in range(n+1)]
    for x,y,pipe_types in edges:
        graph[x].append((y,pipe_types))
        graph[y].append((x,pipe_types))
    
    # BFS 실행
    def bfs(infected,type):
        new_infected = set(infected)
        queue = list(infected)

        while queue:
            node = queue.pop(0) # 첫번째 
            for neighbor,pipe in graph[node]: # 오픈한 파이프와 같고 아직 감염이 안되었다면
                if pipe == type and neighbor not in new_infected: 
                    new_infected.add(neighbor)
                    queue.append(neighbor)
        
        return new_infected # 새로 감염된 배양체를 반환
    
    def dfs(infected,remain_k):
        if remain_k == 0: # 횟수 다 사용했으면
            return len(infected) #감염된 배양체 수
        
        best = len(infected) # 감염된 배양체를 변수에 저장

        for pipe_type in [1,2,3]:
            new_spread = bfs(infected,pipe_type)
            result = dfs(new_spread,remain_k-1) # 횟수 줄이고
            best = max(best,result)
        
        return best
    return dfs({infection}, k)