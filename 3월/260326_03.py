import sys

input = sys.stdin.readline
a = int(input())
t = int(input())
s = input()     # '뻔'이면 0, '데기'면 1
 
arr = ''.join(['0101'+'0'*i + '1'*i for i in range(2, 200)])
idx, cnt = 0, 0

while True:
    if arr[idx] == s:
        cnt += 1 # 몇 번째 뻔 or 몇 번째 데기인가?
    if cnt == t:
        print(idx % a)
        break
    idx += 1

