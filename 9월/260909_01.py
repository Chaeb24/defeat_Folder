def solution(n, goods, reqs):
    answer = [0] * n
    shop_product = {}
    for good in goods:
        l = good.split(" ")
        shop_product[l[0]+"/"+l[1]] = int(l[2]) #사이트/물품 : 가격
    for req in reqs:
        l = req.split(" ")
        buyer = int(l[0])-1 # answer배열에 인덱스로 등록하기 위함.
        buyproduct = l[3][6:]
        shopping_product = l[1]+"/"+l[2]
        if buyproduct.split("/")[1] == l[2]: # 같은 상품인가?
            if shop_product[buyproduct] < shop_product[shopping_product]: # 최저가인가?
                answer[buyer] += shop_product[shopping_product]-shop_product[buyproduct]
    return answer