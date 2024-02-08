class Solution1 {
public:
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        vector <vector <vector <int>>> dp(target+1);
        dp[0]={{}};
        for(int &i:nums)
        {
            for(int j=i;j<=target;j++)
            {
                for(auto v:dp[j-i])
                {
                    v.push_back(i);
                    dp[j].push_back(v);
                }
            }
        }
        return dp[target];
    }
};

class Solution2 {
public:
    vector<vector<int>> res;

    void helper(vector<int>& curr, int idx, int currSum, vector<int>& candidates, int target) {
        if (currSum == target) {
            res.push_back(curr);
            return;
        }

        for (int i = idx; i < candidates.size(); i++) {
            if (currSum + candidates[i] <= target) {
                curr.push_back(candidates[i]);
                helper(curr, i, currSum + candidates[i], candidates, target);
                curr.pop_back();
            }
        }
    }

    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> curr;
        helper(curr, 0, 0, candidates, target);
        return res;
    }
};
