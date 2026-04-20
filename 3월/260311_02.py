# 종 이름 사전 (4358번)
import sys

name = {} # 사전이었고
total = 0 # 전체 값 받아서 뒤에서 나눠줄거라서

for line in sys.stdin:

    if line == '\n': # 띄어쓰기 하면 중지
        break

    tree = line.strip() # 개행 문자 제거
    total += 1 # 입력받으면 total은 증가할거고

    if tree in name: # 사전 안에 종이 있으면
        name[tree] +=1 # 빈도 수만 증가
    else:
        name[tree] = 1 # 등록된 이름 없으면 추가해주면 됨.

# 빈도가 가장 많은 단어를 알파벳순으로 정렬
sorted_tree = sorted(name.keys())

for tree in sorted_tree:  # 소수 4번째 자리까지 반올림해주기
    percentage = round((name[tree]/total)*100,4)
    print(tree, f"{percentage:.4f}")


