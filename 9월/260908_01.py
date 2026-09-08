def solution(seq,k):
    n = len(seq)
    left,right = 0,0
    total = seq[0]

    answer = []

    while right < n:
        if total == k:
            answer.append(right-left,left,right)
            total -= seq[left]
            left +=1 
        elif total < k:
            right += 1
            if right < n:
                total += seq[right]
        else:
            total -= seq[left]
            left += 1

    answer.sort(key=lambda x: (x[0], x[1]))
    return answer[0][1], answer[0][2]
