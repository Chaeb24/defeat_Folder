#2910 문제

N, C = map(int,input().split()) # 입력값 받기
arr = list(map(int, input().split()))

dict_info = {} # 빈도수, 인덱스

for idx, num in enumerate(arr):
    if num not in dict_info:
        dict_info[num] = [idx,1] # 처음등장위치, 빈도수 저장
    else:
        dict_info[num][1] +=1 # 딕셔너리에 있어서 빈도수만 증가

sorted_nums = sorted(dict_info.keys(), key=lambda x: (-dict_info[x][1], dict_info[x][0]))
# dict_info 는 빈도수 내림차순, 인덱스는 오름차순

for num in sorted_nums:
    for _ in range(dict_info[num][1]):
        print(num,end = ' ')

