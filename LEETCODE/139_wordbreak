class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_leaf = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,word):
        node = self.root
        
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node= node.children[c]
        node.is_leaf = True
        
    def search(self,word):
        node = self.root
        for c in word:
            if c not in node.children:
                return False
            node = node.children[c]
        return node.is_leaf       
        
        
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        trie = Trie()
        for word in wordDict:
            trie.insert(word)
            
        dp = [False]*(len(s)+1)
        dp[0] = True
        
        for i in range(1,len(s)+1):
            for j in range(i):
                if dp[j] and trie.search(s[j:i]):
                    dp[i] = True
                    break
        
        return dp[-1]
                