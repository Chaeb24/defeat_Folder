import math
from collections import defaultdict

def get_fees(fees,time):
    # 요금 계산 함수
    default_time,default_fee,unit_time,unit_fee = map(int,fees)

    if time < default_time:
        return default_fee
    else:
        remain = math.ceil((time-default_time) / unit_time)
        return remain * unit_fee + default_fee

def solution(fees,records):
    answer = []
    parking_times = defaultdict(int)

    for record in records:
        # 정보 분리
        time,car,out = record.split()

        hour,minute = map(int,time.split(":"))
        time = hour * 60 + minute

        if out == 'IN':
            parking_times[car] -= time 
            # 없는 키값에 value를 빼면 없는 값이라고 에러가 나는것을 방지
            # defaultdict 사용 이유
        elif out == 'OUT':
            parking_times[car] += time
        else:
            print(f'IN도 OUT도 아님.')
    
    for car, time in sorted(parking_times.items()):
        if time <= 0:
            time += 23 * 60 + 59 # 아직 출차가 안된 상태

        answer.append(get_fees(fees,time))
    
    return answer