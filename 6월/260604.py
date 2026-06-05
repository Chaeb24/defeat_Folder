from itertools import combinations

def solution(n, q, ans):
    answer = 0

    num_list = [i for i in range(1,n+1)] # n개 만큼의 리스트를 만들어준다.

    # num_list에서 랜덤으로 5개를 뽑는다.
    for num in combinations(num_list,5):
        same = []
        
        for check in q: # 제공된 리스트와 com에서 같은 숫자가 있는가
            cnt = 0    
            for i in num:
                if i == check:
                    cnt += 1
            same.append(cnt)
    
        if ans == same:
            answer += 1

    return answer