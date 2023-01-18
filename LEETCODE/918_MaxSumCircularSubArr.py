class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        start, ans = 0, -inf
        length = len(nums)

        while start < length:
            curr = 0 
            for i in range(start,length+start):
                if i < length:
                    curr += nums[i]
                else:
                    curr += nums[(i-length)]
                ans = max(ans,curr)
            start += 1 
        return ans