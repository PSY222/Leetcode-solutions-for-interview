class Solution1 {
public:
    void rotate(vector<int>& nums, int k) {
        vector<int> temp(nums.size());

        for(int i=0; i<nums.size(); i++){
            temp[(i+k)%nums.size()]=nums[i];
        }
        nums=temp;
    }
};

class Solution2 {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        k = k % n;
        std::rotate(nums.begin(), nums.begin() + (n - k), nums.end());
    }
};

//TLE
class Solution3 {
public:
    void rotate(vector<int>& nums, int k) {
        while(k>0){
            int back = nums.back();
            nums.pop_back();
            nums.insert(nums.begin(),back);
            --k;
        }
    }
};