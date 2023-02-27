# 295. Find Median from Data Stream

class MedianFinder:

    def __init__(self):
        self.sh = []
        self.mh = []

    def addNum(self, num: int) -> None:
        if not self.mh or num <= -self.mh[0]:
            heappush(self.mh, -num)
        else:
            heappush(self.sh, num)
        
        if len(self.sh) > len(self.mh):
            heappush(self.mh, -heappop(self.sh))
        elif len(self.mh) > len(self.sh) + 1:
            heappush(self.sh, -heappop(self.mh))
        
    def findMedian(self) -> float:
        if (len(self.sh) + len(self.mh)) %2 == 0:
            return (-self.mh[0] + self.sh[0]) / 2
        return -self.mh[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
