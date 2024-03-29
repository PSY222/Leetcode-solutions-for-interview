#include <vector>
#include <algorithm>

class Solution1 {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int start = 0;
        int min_length = INT_MAX;
        int current_sum = 0; 
        for(int end = 0; end < nums.size(); end ++){
            current_sum += nums[end];
            while (current_sum >= target){
                min_length = min(min_length, end-start+1);
                current_sum -= nums[start];
                start++;
            }
        }
        return min_length == INT_MAX ? 0 : min_length;
    }   
    
};

class Solution2 {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        int l = 0, r = 0, n= nums.size(), sum = 0, len=INT_MAX;
        while (r<n){
            sum += nums[r++];
            while(sum>=target){
                len = min(len, r-l);
                sum -= nums[l++];
            }
        }
        return len == INT_MAX ? 0: len;
    }   
    
};