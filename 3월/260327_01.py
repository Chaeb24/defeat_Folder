# 백준 9079

from sys import stdin
from collections import deque

def solution(arr):
    # 경우의 수 8가지
    cases = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

    visited = [False] * 512
    visited[int(''.join(arr), 2)] = True  # 이진수를 int형으로 변환
	# BFS
    queue = deque([(int(''.join(arr), 2), 0)])
    while queue:
        arrBin, count = queue.popleft()

        if arrBin == 0 or arrBin == 511:
            return count

        for numbers in cases:
            newArr = flip(numbers, list(bin(arrBin)[2:].zfill(9))) # 이진수를 9자리로 변환.
            vs = int(''.join(newArr), 2)
            if not visited[vs]:
                visited[vs] = True
                queue.append((int(''.join(newArr), 2), count+1))
    
    return -1

def flip(numbers, arr):
    for num in numbers:
        arr[num] = '0' if arr[num] == '1' else '1'
    return arr

T = int(stdin.readline())

for _ in range(T):
    arr = list(list(stdin.readline().split()) for _ in range(3))
    arr = ['1' if arr[y][x]=='H' else '0' for y in range(3) for x in range(3)]
    print(solution(arr))