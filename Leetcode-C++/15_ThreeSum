#include <vector>
#include <algorithm>

class Solution1 {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        vector<vector<int>> res;
        set<vector<int>> s;
        sort(nums.begin(),nums.end());
        for(int i=0;i<nums.size()-2;++i){
            int j = i +1;
            int k = nums.size()-1;
            int target = -nums[i];
            while(j<k){
                int twoSum = nums[j] + nums[k];
                if(twoSum==target){
                    s.insert({nums[i],nums[j],nums[k]});
                    j++;
                    k--;
                }else if(twoSum<target){
                    j++;
                }else{
                    k--;
                } 
            }     
        }
        for(auto val: s)
            res.push_back(val);
        return res; 
    } 
};

class Solution2 {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        if (all_of(nums.begin(),nums.end(),[&](const int i) {return i == 0;})) return {{0,0,0}};
        int min = *min_element(nums.begin(), nums.end());
        int max = *max_element(nums.begin(), nums.end()), target;

        if (min >= 0 || max <= 0) return {};
        int range = max - min + 1, exist = 0;
        vector<int> count(range, 0);
        
        for(int& i : nums) ++count[i - min];
        for(int i = 0; i < range; i++){
            if(count[i] !=0) nums[exist++] = i + min;
        }
        vector<vector<int>> triples;
        auto l = nums.begin(), r = next(l, exist - 1);
        while(*l <=0){
            while (*r >= 0){
                target = -(*l + *r);
                if (target < *l) {
                    --r;
                    continue;
                }
                if (target > *r) break;
                if (((*l == target || *r == target) && count[target - min] == 1) || 
                ((*l == target && *r == target ) && count[target - min] == 2)){
                    --r;
                    continue;
                }
                if (count[target - min] !=0 ) triples.push_back({*l, target, *r});
                r--;
            }
            ++l;
            r = next(nums.begin(), exist - 1);
        }
        return triples;
    }
};