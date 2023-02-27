# 2256. Minimum Average Difference

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        ts = sum(nums)
        pf = []
        r = [math.inf, 0]
        
        for i in range(len(nums)):
            if i > 0:
                pf.append(pf[i-1] + nums[i])
            else:
                pf.append(nums[i])
            
            temp = len(nums) - i - 1
            if temp == 0:
                diff = pf[-1]//(i+1)
            else: 
                diff = abs((pf[-1] // (i + 1)) - ((ts - pf[-1]) // (len(nums) - i - 1)))
            
            if diff == r[0]:
                r[1] = min(i, r[1])
                r[0] = diff
            elif diff < r[0]:
                r[1] = i
                r[0] = diff 
        return r[1]
