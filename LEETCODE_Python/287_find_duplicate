class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        dp = [1]*len(nums)
        for i in range(len(nums)):
            dp[nums[i]-1] -= 1
            if dp[nums[i]-1] < 0:
                return nums[i]