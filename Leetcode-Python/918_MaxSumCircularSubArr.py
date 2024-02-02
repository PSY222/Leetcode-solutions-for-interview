#TLE solution
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

#Using Kadane's algorithm plus, making circular into calculation of total-curmin
class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)
        curmax = ans = nums[0]
        curmin = 0
        for num in nums[1:]:
                curmax = max(num, curmax+num)
                curmin = min(num,curmin+num)
                ans = max(ans,curmax,total-curmin)
        return ans
