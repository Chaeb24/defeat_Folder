import heapq

def solution(n,k,enemy):
    removes = [] #무적권을 사용할 적 

    for i in range(len(enemy)): #일단 적의 수 만큼 돌리기
        if len(removes) < k: # 무적권이 남아있다면
            heapq.heappush(removes,enemy[i]) #힙에 적을 넣어버리기
        elif enemy[i] > removes[0]: # 무적권 사용할 적보다 더 많은 적이 있었다면
            n -= heapq.heappop(removes) # 이 적들은 병사들로 무찌르자
            heapq.heappush(removes,enemy[i]) # 더 많은 적을 힙에 넣기
        else: # 현재 적이 무적권을 쓸 만큼 크지 않으므로 병사로 막는다.
            n -= enemy[i] # 그냥 싸우자
    
        if n < 0:
            i -=1   #n이 0보다 아래이면 i 보다 한인덱스 앞이 최선
            break
            
    answer = i+1    #인덱스 맞추기용
    return answer
