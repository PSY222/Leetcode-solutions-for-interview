class Solution {
public:
    vector<vector<int>> res;
    void helper(int idx, vector<int>& nums){   
        int length = nums.size();
        if(idx==length-1){
            res.push_back(nums);
            return;
        }

        for(int i=idx; i <length; i++){
            swap(nums[idx],nums[i]);
            helper(idx+1,nums);
            swap(nums[idx],nums[i]);
        }
    }


    vector<vector<int>> permute(vector<int>& nums) {
        int length = nums.size();
        helper(0,nums);
        return res;
    }
};