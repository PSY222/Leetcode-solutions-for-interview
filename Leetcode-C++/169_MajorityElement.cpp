#include <vector>

class Solution{
    public:
        int majorityElement(std::vector<int>& nums){
            int majority = nums[0];
            int cnt = 1;
            for(int i=1; i<nums.size(); ++i){
                if(nums[i] == majority){
                    ++cnt;
                }else if(cnt==0){
                    majority = nums[i];
                    cnt = 1;
                }else{
                    --cnt;
                }
            }
            return majority;
        }
};