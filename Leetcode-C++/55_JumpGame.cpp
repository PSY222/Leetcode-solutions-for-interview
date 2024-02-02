class Solution {
public:
    bool canJump(vector<int>& nums) {
        int size = nums.size();
        vector<bool> dp(size,false);
        dp[0] = true;
        for(int i=1; i<size; i++){
            for(int j = i-1; j >= 0; j--){
                if(dp[j] && j + nums[j]>=i){
                    dp[i]=true;
                    break;
                }
            }
        }
        return dp[size-1];      
    }
};