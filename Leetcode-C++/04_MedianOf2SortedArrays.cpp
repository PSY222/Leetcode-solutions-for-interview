class Solution {
public:
    double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
        if(nums1.size()>nums2.size()){
            return findMedianSortedArrays(nums2,nums1);
        }

        int m = nums1.size(), n = nums2.size();
        int left = 0, right =m;

        while(left<=right){
            int midA = (left+right)/2;
            int midB = (m+n+1)/2-midA;

            int leftA = (midA == 0) ? INT_MIN : nums1[midA-1];
            int rightA = (midA==m) ? INT_MAX : nums1[midA];
            int leftB = (midB ==0) ? INT_MIN : nums2[midB-1];
            int rightB = (midB == n) ?INT_MAX : nums2[midB];

            if(leftA <= rightB && leftB <= rightA){
                if((m+n)%2==0){
                    return (max(leftA,leftB)+min(rightA,rightB))/2.0;
                }else{
                    return max(leftA,leftB);
                }
            }else if (leftA>rightB){
                right = midA -1;
            }else{
                left = midA +1;
            }
        }
        return 0.0;
    }
};

