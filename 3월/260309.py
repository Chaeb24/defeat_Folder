# 4659번

# 모음
vowel = ['a','e','i','o','u']

while True:
    s = input()
    if s == 'end':
        break

    acceptable = True
    has_vowel = False
    s_list = list(s)

    # 모음 포함 여부 체크
    for c in s_list:
        if c in vowel:
            has_vowel = True
            break

    # 3연속 모음/자음 체크
    for i in range(len(s_list)-2):
        if (s_list[i] in vowel and s_list[i+1] in vowel and s_list[i+2] in vowel) or \
           (s_list[i] not in vowel and s_list[i+1] not in vowel and s_list[i+2] not in vowel):
            acceptable = False
            break

    # 2연속 같은 문자 체크 (ee, oo만 허용)
    for i in range(len(s_list)-1):
        if s_list[i] == s_list[i+1]:
            if s_list[i] not in ['e', 'o']:
                acceptable = False
                break

    if not has_vowel:
        acceptable = False

    if acceptable:
        print(f'<{s}> is acceptable.')
    else:
        print(f'<{s}> is not acceptable.')
