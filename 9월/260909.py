def solution(name, yearning, photo):
    answer = []
    
    zipped = dict(zip(name,yearning))# 이름과 점수 딕셔너리로 만들기
    
    for p in photo:
        sum = 0
        for person in p:
            sum += zipped.get(person,0) # 사전에 이름이 있는가?
        answer.append(sum) # 들여쓰기에 유의
    
    return answer