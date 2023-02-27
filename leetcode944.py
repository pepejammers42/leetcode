# 944. Delete Columns to Make Sorted

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        vert = zip(*strs)
        result = 0
        for v in vert:
            if list(v) != sorted(v):
                result += 1
        return result
