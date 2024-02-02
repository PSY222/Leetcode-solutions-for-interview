class Solution:
    
    def orangesRotting(self, grid: List[List[int]]) -> int:
        visited = []
        r, c = len(grid), len(grid[0])
        mins = 0
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0:
                    visited.append((i,j))
                if grid[i][j] == 2:
                    self.bfs(grid,i,j,visited)
                    mins += 1
                    
        if any(1 in i for i in grid):
            return -1
        else:
            return grid, mins
                    
    def bfs(self,grid,i,j,visited):
        r, c = len(grid), len(grid[0])
        dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        q = deque([(i,j)])
        visited.append((i,j))
    
        while q:
            a, b = q.popleft()
            for x, y in dir:
                newa = a+x
                newb = b+y
                if 0 <= newa <r and 0 <= newb <c and grid[newa][newb] not in visited:
                    if grid[newa][newb] == 0:
                        continue
                    if grid[newa][newb] == 2:
                        q.append((newa,newb))
                        continue
                    else:
                        grid[newa][newb] = 2
                        q.append((newa,newb))
                    visited.append((newa,newb))
                
                
            
        