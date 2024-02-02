class Solution {
public:
    int numIdenticalPairs(vector<int>& nums) {
        unordered_map<int,int> record;
        int ans = 0;

        for(int i=0; i < nums.size() ; i++){
            record[nums[i]] += 1;
        }

        for(auto& kvp: record){
            int n = kvp.second; 
            ans += n*(n-1)/2;
        }

        return ans;
    }

};