# 169. Majority Element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        can = None
        
        for n in nums:
            if cnt == 0:
                can = n
            cnt += (1 if n == can else -1)
        return can