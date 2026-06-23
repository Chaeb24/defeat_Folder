def solution(diffs, times, limit):
    left = 1
    right = max(diffs)
    answer = right

    # 이진 탐색
    while left <= right:
        mid_level = (left+right)//2
        total_time = 0

        for i in range(len(diffs)):
            if diffs[i] <= mid_level:
                total_time += times[i] # 난이도가 가장 낮은 경우 1
            else:
                cnt = diffs[i] - mid_level # 인덱스 벗어날 일 없음.
                total_time += (times[i] + times[i-1]) * cnt + times[i]
    
        if total_time <= limit:
            answer = mid_level
            right = mid_level - 1  # 더 작은 숙련도가 있는지 왼쪽 구간 탐색
        else:
            left = mid_level + 1   # 시간이 초과됐으므로 숙련도를 높여야 함
    
    return answer
    
    