class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        prev_min,prev_max,maxres = nums[0], nums[0], nums[0]
        if len(nums) == 1:
            return nums[0]
        
        for n in nums[1:]:
            curr_min = min(prev_max*n,prev_min*n,n)
            curr_max = max(prev_max*n,prev_min*n,n)
            maxres = max(maxres,curr_max)
            prev_max = curr_max
            prev_min = curr_min
        return maxres