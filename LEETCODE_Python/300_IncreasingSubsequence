class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp = [1]*len(nums)
        # for i in range(len(nums)):
        #     for j in range(i):
        #         if nums[i] > nums[j] and dp[i] <dp[j] +1:
        #             dp[i] = dp[j] + 1
        # return max(dp)
        
        long = []
        for i in nums:
            if len(long) == 0 or long[-1] < i:
                long.append(i)
            else:
                idx = bisect_left(long,i)
                long[idx] = i
        return len(long)
        