def solution(n, m, amount):
    result = []

    for _ in range(n):
        # 참가자 금액 내림차순 정렬
        sorted_amount = sorted(amount, reverse=True)

        first_max = sorted_amount[0]
        second_max = sorted_amount[1] if len(sorted_amount) > 1 else 0

        # 최고 금액 참가자 인덱스
        target_index = amount.index(first_max)

        # 낙찰가
        selected_price = second_max + 10000
        if selected_price > first_max:
            selected_price = first_max

        # 금액 차감
        amount[target_index] -= selected_price

        result.append(selected_price)

    return result

n = 6
m = 3
amount = [30000,70000, 10000]

print(solution(n, m, amount))