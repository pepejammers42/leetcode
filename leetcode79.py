# 79. Word Search

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row, col = len(board), len(board[0])
        R, C, visited = range(row), range(col), set()

        def dfs(loc, i=0):
            
            if len(word) == i:
                return True
            
            r,c = loc

            if (r not in R or c not in C or 
                loc in visited            or 
                board[r][c] != word[i]): return False
            
            visited.add(loc)

            res = (dfs((r+1,c), i+1) or dfs((r,c+1), i+1) or
                   dfs((r-1,c), i+1) or dfs((r,c-1), i+1))
            
            visited.remove(loc)

            return res

        
        return any(dfs((r, c))  for c in C for r in R)
