# 57. Insert Interval
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s, e = 0, 0
        for c,v in enumerate(intervals):
            if newInterval[0] > v[1]:
                s += 1
            else:
                break
        e = s
        for i in range(e, len(intervals)):
            if newInterval[1] > intervals[i][1]:
                e += 1
            else:
                break

        ns, ne = None, None
        td = e - s + 1
        
        if s >= len(intervals) or newInterval[0] < intervals[s][0] or newInterval[0] > intervals[s][1]:
            ns = newInterval[0]
        else:
            ns = intervals[s][0]
            
        if e >= len(intervals) or newInterval[1] < intervals[e][0] or newInterval[1] > intervals[e][1]:
            ne = newInterval[1]
        else:
            ne = intervals[e][1]
        if e < len(intervals) and newInterval[1] < intervals[e][0]:
            td -= 1
            print('hit here')
        
        print(e, s)
        print(ns, ne)
        if s < len(intervals):
            for _ in range(td):
                if len(intervals) > 1:
                    intervals.pop(s)
    
        intervals.insert(s, [ns, ne])
        return intervals
        

