class Solution{
    public:
        int longestSubarray(vector<int>& nums){
            int limit = 1;
            int start=0, end=0, zeroCnt=0, res=0;

            for(int end=0; end < nums.size(); ++end){
                if(nums[end]==0){
                    zeroCnt++;
                }

                while(zeroCnt > limit){
                    if(nums[start++]==0){
                        zeroCnt--;
                    }
                }
                res = max(res,end-start);
            }
            return res;
        }
}