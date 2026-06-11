def solution(edges):
    def count_edges(edges):
        edge_count={}
        for a,b in edges:
            if not edge_count.get(a):
                edge_count[a] = [0,0]
            if not edge_count.get(b):
                edge_count[b] = [0,0]
        # a->b로 이동하므로
        edge_count[a][0] += 1
        edge_count[b][1] += 1
        return edge_count
    
    def check_answer(edge_counts):
        answer = [0,0,0,0]

        for key,count in edge_counts.items():
            if count[0] >= 2 and count[1] == 0: # 생성된 정점 노드
                answer[0] = key
            elif count[0] == 0 and count[1] > 0: # 막대그래프
                answer[2] += 1
            elif count[0] >= 2 and count[1] >= 2:
                answer[3] += 1  # 8자 그래프 카운트
            
            answer[1] = (edge_counts[answer[0]][0] - answer[2] - answer[3])
        return answer