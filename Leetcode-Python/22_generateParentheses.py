class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(s='', left=0, right=0):
            if len(s) == 2*n:
                res.append(s)
                return
            if left < n:
                backtrack(s+'(', left+1, right)
            if right < left:
                backtrack(s+')', left, right+1)
        backtrack()
        return res
        

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        self.dfs(n,n,res,'')
        return res
    
    def dfs(self,l,r,res,curr):
        if r < l:
            return
        if not l and not r:
            return res.append(curr)
        if l:
            self.dfs(l-1,r,res,curr+'(')
        if r:
            self.dfs(l,r-1,res,curr+')')
            
        