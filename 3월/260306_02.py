T = int(input())

# 스택 문제
for _ in range(T):
    line = input()
    count = 0
    is_valid = True

    for ch in line:
        if ch == '(': # 문자열에서 괄호 시작과 끝의 개수가 같은가
            count += 1
        else:
            count -= 1
        # 중간 점검 필요
        if count < 0:
            is_valid = False
            break

    if is_valid and count == 0:
        print("YES")
    else:
        print("NO")
