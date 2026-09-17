def solution(ings,menu,sell):
    answer = 0

    making = {} # 재료별 금액
    for ing in ings:
        l = ing.split(" ")
        making[l[0]] = int(l[1])

    menu_ing = {} # 메뉴별 수익 계산
    for men in menu:
        l = men.split(" ")
        hap = 0
        for ze in l[1]:
            hap += making[ze]
        menu_ing[l[0]] = int(l[2]) - hap

    for sel in sell:
        l = sel.split(" ")
        answer += menu_ing[l[0]] * l[1] #금액을 계산하면

    return answer