class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        l, r, t, b= 0, n-1, 0, m-1
        res = []
        
        while l <= r and t <= b:
            for col in range(l,r+1):
                res.append(matrix[t][col])
            t += 1
            for row in range(t,b+1):
                res.append(matrix[row][r])
            r -= 1
            for col in range(r,l-1,-1):
                res.append(matrix[b][col])
            b -= 1
            for row in range(b,t-1,-1):
                res.append(matrix[row][l])
            l += 1
        return res[:m*n]

                    
