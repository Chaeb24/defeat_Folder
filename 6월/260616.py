T = int(input())

def check(s):
    
    n_count = s.count('N')
    s_count = s.count('S')
    e_count = s.count('E')
    w_count = s.count('W')
    
    # 북쪽으로 간 횟수와 남쪽으로 간 횟수가 같고,
    # 동쪽으로 간 횟수와 서쪽으로 간 횟수가 같아야 제자리로 돌아옴!
    return (n_count == s_count) and (e_count == w_count)

for tc in range(1, T + 1):
    command = input().strip()
    
    if check(command):
        print(f"Yes")
    else:
        print(f"No")