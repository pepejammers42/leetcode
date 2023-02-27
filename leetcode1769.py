# 1769. Minimum Number of Operations to Move All Balls to Each Box

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        l = len(boxes)
        r = [0] * l
        pos = 0
        right = 0
        left = 0

        for i in range(l):
            if boxes[i] == '1':
                pos += i
                right += 1
        
        for i in range(l):
            r[i] = pos
            
            if boxes[i] == '1':
                right -= 1
                left += 1
            
            pos += left - right
        return r
