# 1282. Group the People Given the Group Size They Belong To

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        d = defaultdict(list)
        
        for k, v in enumerate(groupSizes):
            d[v].append(k)
        
        r = []
        
        for k,v in d.items():
            if len(v) > k:
                for i in range(0, len(v)//k):
                    r.append(v[i*k:(i+1)*k])
            else:
                r.append(v)
        return r 
