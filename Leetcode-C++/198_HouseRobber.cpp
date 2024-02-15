class Solution1 {
public:
    int solve(vector<int>& nums,int i,int n,vector<int>& dp)
    {
        if(i>=n) return 0;
        if(dp[i]!=-1) return dp[i];
        int include = nums[i] + solve(nums,i+2,n,dp);
        int exclude = 0 + solve(nums,i+1,n,dp);
        return dp[i] =  max(include,exclude);
    }
    int rob(vector<int>& nums) {
        int n = nums.size();
        vector<int>dp(n+1,-1);
        
        return solve(nums,0,n,dp);
    }
};

class Solution2 {
public:
    int rob(vector<int>& nums) {
        int n = nums.size();
        if(n==0) return 0;

        vector<int> dp(n+1,0);
        dp[1] = nums[0];
        for(int i=2; i<=n ; i++){
            dp[i] = max(dp[i-1],dp[i-2]+nums[i-1]);
        }
        return dp[n];
    }
};