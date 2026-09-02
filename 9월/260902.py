word_du = ['salar', 'salay', 'salry', 'saary', 'slary', 'alary'] # 단어에서 한 글자씩 누락된 경우의 수

def is_sal(name):
    # salary가 다 포함된 경우
    if "salary" in name:
        return True

    # 한글자씩 누락된 경우
    for w in word_du:
        if w in name:
            return True

    # 전체 글자(name)에서 확인하고 싶은 단어길이만큼 빼고 +1 하기
    for j in range(0,len(name)-5):
        sub=name[j:j+6]
        count = 0
        for i in range(6):
            if sub[i] == "salary"[i]:
                count+=1 

        if count<=1:
            return True

    return False