def solution(s, skip, index):
    answer = ''

    for word in s:
        cur_word = ord(word) #아스키 코드로 전환
        count = 0

        while count < index:
            cur_word += 1

            if cur_word == ord('z'):
                cur_word = ord('a') # z를 넘어가면 a로 변경

            if cur_word not in skip:
                count += 1 # skip 알파벳에 없으면 횟수를 더해줘도 됨.
        answer += chr(cur_word)

    return answer