from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        answer = []

        for i in range(len(nums)):
            while q and nums[q[-1]]<=nums[i]: # 새로 들어온 수가 덱의 뒤에 있는 수보다 작을때
                q.pop()
            q.append(i) # 그게 아니면 덱에 추가
            if q[0] <= i-k: # 슬라이딩 윈도우 범위 벗어났으면
                q.popleft() # 윈도우 크기 맞춰주기
            
            if i >= k - 1:
                # 덱의 맨 앞(q[0])에 있는 인덱스의 값이 무조건 최솟값
                answer.append(nums[q[0]])
        
        return answer