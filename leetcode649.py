class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        d = deque()
        r = deque()
        l = len(senate)
        
        for c, v in enumerate(senate):
            if v == 'R':
                r.append(c)
            else:
                d.append(c)
        
        while len(d) > 0 and len(r) > 0:
            a, b = d.popleft(), r.popleft()
            if a > b:
                r.append(l + b)
            else:
                d.append(l + a)
        
        return "Radiant" if len(r) > 0 else "Dire"
