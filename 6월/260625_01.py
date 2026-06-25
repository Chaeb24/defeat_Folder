def solution(video_len, pos, op_start, op_end, commands):
    # 분을 싹 다 초로 변환
    def min_to_sec(t):
        m,s = map(int,t.split(":"))
        return m * 60 + s

    # 초를 문자열로 변환
    def s_to_str(sec):
        m = sec // 60
        s = sec % 60 # 남은 초
        if m < 10:
            m = f'0{m}'
        if s <10:
            s = f'0{s}'
        return f"{m}:{s}"
    
    # 일단 싹 다 초로 바꿔주기
    video = min_to_sec(video_len)
    now = min_to_sec(pos)
    os_ = min_to_sec(op_start)
    oe_ = min_to_sec(op_end)

    # 명령어 실행
    for command in commands:
        if os_ <= now <= oe_: # 오프닝 구역에 있다면
            now = oe_ # 끝나는 부분으로 옮겨주기
        
        # 버튼이 next, prev에 따라 10초 움직임
        if command == "next":
            now += 10
        else:  # "prev"
            now -= 10

        # 0보다 작으면 0으로 보정
        if now < 0:
            now = 0
        # 영상 길이 초과하면 끝으로 고정
        if now > video:
            now = video
    
     # 마지막 위치도 오프닝 구간에 걸치면 엔딩 시점으로
    if os_ <= now <= oe_:
        now = oe_

    # 영상 끝을 넘기면
    if now >= video:
        return video_len
    return s_to_str(now)
