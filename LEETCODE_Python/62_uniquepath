class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = [[-1 for i in range(n)] for j in range(m)]
        return self.path(matrix,0,0,m-1,n-1)
    
    def path(self,matrix,i,j,m,n):
        if i ==m and j==n:
            return 1
        
        if matrix[i][j] == -1:
            down, right = 0, 0
            if i < m:
                down = self.path(matrix,i+1,j,m,n)
            if j <n :
                right = self.path(matrix,i,j+1,m,n)
            matrix[i][j] = down + right
        return matrix[i][j]