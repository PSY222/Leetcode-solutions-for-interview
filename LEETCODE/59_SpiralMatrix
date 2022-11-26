# Got idea from Neetcode YouTube video
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        mtrx = [[0] * n for _ in range(n)]
        l = top = 0
        r = bot = n
        start = 1
        
        while l < r and top < bot:
            for i in range(l,r):
                mtrx[top][i] = start
                start += 1
            top += 1
            
            for i in range(top,bot):
                mtrx[i][r-1]= start
                start += 1
            r -= 1
            if not (l<r and top<bot):
                break
            for i in range(r-1,l-1,-1):
                mtrx[bot-1][i] = start
                start +=1 
            bot -= 1
            for i in range(bot-1,top-1,-1):
                mtrx[i][l] = start
                start +=1
            l += 1
        return mtrx
            
#Source: https://leetcode.com/problems/spiral-matrix-ii/discuss/22282/4-9-lines-Python-solutions        

    def generateMatrix(self, n):        
        res, lo = [[n*n]], n*n
        while lo > 1:
            lo, hi = lo -len(res), lo
            res = [[i for i in range(lo,hi)]] + [list(j) for j in zip(*res[::-1])]
        return res
   
    def generateMatrix(self, n):
        A = [[0] * n for _ in range(n)]
        i, j, di, dj = 0, 0, 0, 1
        for k in range(n*n):
            A[i][j] = k + 1
            if A[(i+di)%n][(j+dj)%n]:
                di, dj = dj, -di
            i += di
            j += dj
        return A