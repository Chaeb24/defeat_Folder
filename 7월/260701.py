def solution(n, times):
    answer = 0

    left = 0
    right = max(times) * n

    while left <= right:
        mid = (left + right) // 2

        total = 0
        for t in times:
            total += mid // t # 몇 명을 심사할 수 있는지 저장

        if total >= n:
            answer = mid          # 가능한 시간이므로 저장
            right = mid - 1       # 더 짧은 시간도 가능한지 탐색
        else:
            left = mid + 1        # 시간이 부족하므로 늘림

    return answer