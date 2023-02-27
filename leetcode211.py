class WordDictionary:

    def __init__(self):
        self.child = {}
        self.end = False
        self.l = 0

    def addWord(self, word: str) -> None:
        curr = self
        for ch in word:
            if ch not in curr.child:
                curr.child[ch] = WordDictionary()
                curr.child[ch].l = len(word) - 1
            curr = curr.child[ch]
        curr.end = True
        self.l = max(self.l, len(word))

    def search(self, word: str) -> bool:
        if self.l < len(word):
            return False
        
        def dfs(obj, word):
            curr = obj
            
            for i, ch in enumerate(word):
                if ch == '.':
                    for sub in curr.child: 
                        if dfs(curr.child[sub], word[i+1:]):
                            return True
                    return False
                else:
                    if ch not in curr.child:
                        return False
                    curr = curr.child[ch]
            return curr.end
        
        return dfs(self, word)
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)