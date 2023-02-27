# 134. Gas Station

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        ind = 0
        curr_vol = 0

        for i in range(len(gas)):
            curr_vol += gas[i]-cost[i]
            if curr_vol < 0:
                curr_vol = 0
                ind = i + 1
        return ind
