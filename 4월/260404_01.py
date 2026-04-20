import sys
input = sys.stdin.readline

def solution():
    N, K = map(int, input().split())
    arr = list(map(int, input().split()))

    left = max(arr)     # 어떤 구간이든 최소 이 값은 되어야 함
    right = sum(arr)    # 최악은 전부 한 구간
    answer = right

    while left <= right:
        mid = (left + right) // 2

        count = 1       # 현재 만든 구간 수
        current_sum = 0

        for num in arr:
            # 현재 구간에 num을 넣으면 mid 초과
            if current_sum + num > mid:
                count += 1
                current_sum = num
            else:
                current_sum += num

        # K개 이하로 나눌 수 있으면 가능
        if count <= K:
            answer = mid
            right = mid - 1
        else:
            left = mid + 1

    print(answer)

solution()