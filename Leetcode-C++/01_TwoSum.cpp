#include <vector>
#include <algorithm>

class Solution1 {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        for(int i=0; i<nums.size(); i++){
            for(int j=i+1; j<nums.size(); j++){
                if(nums[i]+nums[j] == target){
                    return {i,j};
                }
            }
        }
        return {};
    }
};

class Solution2 {
public:
    vector<int> twoSum(vector<int>& nums, int target){
        unordered_map<int, int> numMap;
        int n = nums.size();

        for(int i=0; i<n; i++){
            numMap[nums[i]] = i;
        }

        for(int i=0; i<n; i++){
            int complement = target - nums[i];
            if(numMap.count(complement) && numMap[complement] != i){
                return {i, numMap[complement]};
            }
        }
        return {};
    }
};

class Solution3 {
    public:
        vector<int> twoSum(vector<int>& nums, int target){
            unordered_map<int,int> indices;
            for(int i=0; i<nums.size(); i++){
                if(indices.find(target-nums[i]) != indices.end()){
                    return {indices[target-nums[i]],i};
                }
                indices[nums[i]] = i;
            }
            return {};
        }
};