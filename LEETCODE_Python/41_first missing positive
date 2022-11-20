class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        ans = 1
        nums = list(set(nums))
        for i in range(len(nums)):
            curr = heappop(nums)
            if curr >0 and curr <= ans:
                ans += 1
        return ans
        