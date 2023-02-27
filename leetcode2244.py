# 2244. Minimum Rounds to Complete All Tasks

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        cnt = Counter(tasks)
        res = 0 

        for v in cnt.values():
            if v == 1:
                return -1
            res += math.ceil(v/3)
        
        return res        
