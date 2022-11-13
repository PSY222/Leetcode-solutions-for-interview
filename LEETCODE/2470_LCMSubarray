from math import lcm
class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        ans = 0
          
        for i in range(len(nums)):
            curr = nums[i]
            for j in range(i, len(nums)):
                curr = lcm(curr,nums[j])
                if curr == k:
                    ans += 1
        return ans
    
    