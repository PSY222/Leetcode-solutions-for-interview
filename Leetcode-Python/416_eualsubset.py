class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @cache #memoization
        def subset(s,i=0):
            if s == 0: return True
            if i>=len(nums) or s <0: return False
            return subset(s-nums[i],i+1) or subset(s,i+1)
        total_sum = sum(nums)
        return total_sum & 1 ==0 and subset(total_sum//2)