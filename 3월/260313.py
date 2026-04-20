import sys
nums = sys.stdin.readline().rstrip()
n = 0
idx = 0
while True:
    n += 1
    for s in str(n): # n의 각 자리 수를 s로 순회
        if nums[idx] == s: # nums의 idx 번째 수가 s와 같다면
            idx += 1
            if idx >= len(nums):
                print(n)
                exit()