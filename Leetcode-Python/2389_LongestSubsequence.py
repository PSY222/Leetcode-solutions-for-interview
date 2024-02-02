class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]

        ans = []

        for q in queries:
            idx = bisect.bisect(nums,q)
            ans.append(idx)
        
        return ans

#Java version
class Solution {
    public int[] answerQueries(int[] nums, int[] queries) {
        Arrays.sort(nums);
        for(int i=1; i < nums.length; ++i)
            nums[i] += nums[i-1];

        int n = queries.length;
        int ans[] = new int[n];
        for(int i=0; i < n; ++i){
            int idx = binarySearch(nums,queries[i]);
            ans[i] = idx;
        }
        return ans;
    }
    int binarySearch(int[] nums, int target){
        int l = 0, r = nums.length-1;
        while (l<r){
            int mid = (l+r)/2;
            if(nums[mid]==target)
            return mid +1;
            if (nums[mid]<target)
            l = mid+1;
            else
            r = mid -1;
        }
        return nums[l] > target? l : l+1;
    }
}