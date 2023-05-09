class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        m = len(mat)
        res = 0
        for i in range(m): 
            res += mat[i][i] + mat[i][m-i-1]
        if m % 2 == 1:
            res -= mat[m//2][m//2]
        return res
