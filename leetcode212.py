class Node:
    def __init__(self):
        self.child = {}
        self.end = False
class Trie:
    def __init__(self):
        self.root = Node()
    
    def insert(self, word: str):
        curr = self.root
        
        for ch in word:
            if ch not in curr.child:
                curr.child[ch] = Node()
            curr = curr.child[ch]
        curr.end = True
    
    def search(self, word: str):
        curr = self.root
        
        for ch in word:
            if ch not in curr.child:
                return False
            curr = curr.child[ch]
        return curr.end

    def startsWith(self, prefix: str):
        curr = self.root
        
        for ch in prefix:
            if ch not in curr.child:
                return False
            curr = curr.child[ch]
        return True
    
class Solution:
        def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
            t = Trie()
            for w in words:
                t.insert(w)
            output = []
            row, col = len(words), len(words[0])
            
            def dfs(r, c, l):
                if 0 > r or r >= row or 0 > c or c >= col or board[r][c] == 0:
                    return
                merge = l + [board[r][c]]
                as_str = "".join(merge)
                if not t.startsWith(as_str):
                    return 
                elif t.search(as_str) and as_str not in output:
                    output.append(as_str)
                
                prev = board[r][c]
                board[r][c] = 0
                dfs(r + 1, c, merge)
                dfs(r - 1, c, merge)
                dfs(r, c + 1, merge)
                dfs(r, c - 1, merge)
                board[r][c] = prev
                
            for i in range(row):
                for j in range(col):
                    dfs(i, j, [])

            return output