class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dir = [(1,0),(0,1),(0,-1),(-1,0)]
        m,n = len(matrix), len(matrix[0])

        @lru_cache(maxsize=None)
        def dfs(r,c):
            ans = 1
            for (nr, nc) in dir:
                new_r = r+nr
                new_c = c+nc
                if 0 <= new_r < m and 0 <= new_c <n and matrix[new_r][new_c] > matrix[r][c] :
                    ans = max(ans,dfs(new_r,new_c)+1)
            return ans

        return max(dfs(r,c) for r in range(m) for c in range(n))


#Leetcode top solution source: https://leetcode.com/problems/longest-increasing-path-in-a-matrix/submissions/855884352/
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]: return 0
        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]
        
        def dfs(i, j):
            if not dp[i][j]:
                val = matrix[i][j]
                dp[i][j] = 1 + max(
                    dfs(i - 1, j) if i and val > matrix[i - 1][j] else 0,
                    dfs(i + 1, j) if i < m - 1 and val > matrix[i + 1][j] else 0,
                    dfs(i, j - 1) if j and val > matrix[i][j - 1] else 0,
                    dfs(i, j + 1) if j < n - 1 and val > matrix[i][j + 1] else 0)
            return dp[i][j]
        
        return max(dfs(x, y) for x in range(m) for y in range(n))
