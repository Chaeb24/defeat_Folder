def Solution(players,callings):
    # 딕셔너리를 만들어서 플레이어 : 0등인지 저장
    player_dic = {player: i for i,player in enumerate (players)}

    for c in callings:
        idx = player_dic[c] # 불려진 플레이어는 몇 등인가
        front = players[idx-1] # 앞 플레이어는 누구인가

        # 순서를 바꿔준다.
        players[idx-1],players[idx] = players[idx],players[idx-1]

        # 딕셔너리를 업데이트 해준다
        player_dic[c] -= 1
        player_dic[front] += 1

    return players

    
