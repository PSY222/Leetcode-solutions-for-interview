class Solution1 {
public:
    int minPathSum(vector<vector<int>>& grid) {
     int r = grid.size(), c = grid[0].size();

     for(int i=1; i<r; i++)
        grid[i][0] += grid[i-1][0];

    for(int j=1; j<c; j++)
        grid[0][j] += grid[0][j-1];

    for(int i=1; i<r; i++)
        for(int j=1; j<c; j++)
            grid[i][j] += min(grid[i-1][j], grid[i][j-1]);

    return grid[r-1][c-1];
    }
};

class Solution2{
    public:
        int helper(vector<vector<int>>& grid, vector<vector<int>>& dp, int m, int n){
            if(m==0 && n==0) return grid[0][0];
            if(m<0 || n<0) return 1e5;
            if(dp[m][n]) return dp[m][n];
            int up = helper(grid,dp,m-1,n)+grid[m][n];
            int left = helper(grid,dp,m,n-1)+grid[m][n];
            dp[m][n] = min(up,left);
            return dp[m][n];
        }

        int minPathSum(vector<vector<int>>& grid){
            int m = grid.size();
            int n = grid[0].size();
            vector<vector<int>> dp(m,vector<int>(n,0));
            return helper(grid,dp,m-1,n-1);
        }
}