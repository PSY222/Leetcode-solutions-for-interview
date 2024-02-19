class Solution {
public:
    int maxArea(vector<int>& height) {
        int left = 0, right = height.size()-1;
        int store;
        while(left < right){
            int curr = (right-left)*min(height[left],height[right]);
            store = max(curr,store);
            if(height[left]<height[right]){
                ++left;
            }else{
                --right;
            }
        }
        return store;
    }
};