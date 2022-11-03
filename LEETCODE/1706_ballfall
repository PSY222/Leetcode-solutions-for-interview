class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m , n = len(grid), len(grid[0])
        answer = []
        if m == 1 and n ==1:
            return [-1]
        
        def dfs(row,col):
            if row == m:
                return col

            move = col + grid[row][col]
            if move == -1 or move == n or grid[row][move] != grid[row][col]:
                return -1
            return dfs(row+1,move)     
        
        for c in range(n):
            answer.append(dfs(0,c))
        return answer
                
        
    
       