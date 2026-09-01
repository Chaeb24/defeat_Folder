#백트래킹, bruteforce 문제

def solution(donation):
    m = len(donation) #전체 회차 수
    n = len(donation[0]) # 전체 사람 수

    suspects_per_round = []
    for r in range(m):
        my_money = donation[r][0] #내가 항상 0번째 참가자
        suspects = set()

        for p in range(1,n):
            if donation[r][p] == my_money:
                suspects.add(p) #나랑 같은 금액을 내는 사람을 스파이목록에 추가

        suspects_per_round.append(suspects)

    def search(round_idx, current_suspects):
        if round_idx == m:
            return 0

        #돈을 낸 경우
        money_if_pay = 0 + search(round_idx+1, current_suspects)

        #돈을 내지 않은 경우
        next_suspects = current_suspects & suspects_per_round[round_idx]

        money_if_skip = 0
        if len(next_suspects)>0:
            saved_money = donation[round_idx][0]
            money_if_skip = saved_money + search(round_idx+1,next_suspects)

        return max(money_if_pay,money_if_skip)

    all_players = set(range(1,n))

    return search(0,all_players)