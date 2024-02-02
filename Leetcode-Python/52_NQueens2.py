class Solution:
    def totalNQueens(self, n: int) -> int:
        res = []
        l_diag = r_diag = []
        
        def btr(r,path,l_diag,r_diag):
            if len(path) == n:
                res.append(path)
                return
            for c in range(n):
                if c not in path and r-c not in l_diag and r+c not in r_diag:
                    btr(r+1,path+[c],l_diag +[r-c],r_diag + [r+c])
                    
        btr(0,[],l_diag,r_diag)
        return len(res)
            
# BackTracking code (patrick40, https://leetcode.com/problems/n-queens-ii/discuss/126533/Python-Backtracking-Solution-(Beats-97))
class Solution:
    def totalNQueens(self, n: int, diag1=set(), diag2=set(), cols=set(), row=0) -> int:
        if row == n: return 1
        count = 0
        for col in range(n):
            if row+col in diag1 or row-col in diag2 or col in cols: continue
            diag1.add(row+col)
            diag2.add(row-col)
            cols.add(col)
            
            count += self.totalNQueens(n, diag1, diag2, cols, row + 1)
            
            diag1.remove(row+col)
            diag2.remove(row-col)
            cols.remove(col)
        return count