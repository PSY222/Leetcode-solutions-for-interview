class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = [] ;  cols = l_diag = r_diag = set()
		
        def btr(r,pos,l_diag,r_diag): 
            base = "."*n
            if len(pos) == n:
                res.append([base[:i]+"Q"+base[i+1:] for i in pos])
                return
            for c in range(n):
                if not c in pos and not r - c in l_diag and not r + c in r_diag:
                    btr(r+1,pos+[c],l_diag+[r-c],r_diag+[r+c])
                    
        btr(0,[], [],[])
        return res