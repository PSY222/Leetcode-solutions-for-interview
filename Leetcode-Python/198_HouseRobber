class Solution:
    def rob(self, nums: List[int]) -> int:
        #length can be min 1
        #return maximum amount of money
        leng = len(nums)
        
        if leng==0:
            return 0
        if leng==1:
            return nums[0]
        if leng==2:
            return max(nums)
        
        dp = [0]*leng
        dp[0], dp[1] = nums[0], max(nums[0],nums[1])
        
        for i in range(2,leng):
            dp[i] = max(dp[i-2]+nums[i],dp[i-1])
        return dp[-1]