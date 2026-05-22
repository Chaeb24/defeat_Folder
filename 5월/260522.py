def solution(players, m, k): # k는 서버1개당 시간
    answer = 0

    server = 0
    expire = [0] * (len(players) + k + 1) # 서버 증설 후 k시간까지 유지되는 거 표시

    for time in range(len(players)):

        # 종료될 서버 반영
        server -= expire[time]

        # 현재 필요한 서버 수
        need = players[time] // m # m 명당 1개 서버 필요

        # 부족하면 증설
        if need > server:
            add = need - server

            answer += add
            server += add

            # k시간 뒤 종료
            expire[time + k] += add

    return answer