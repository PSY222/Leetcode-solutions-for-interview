class Solution:
    def sortColors(self, nums: List[int]) -> None:

        #[heappop(nums) for i in range(len(nums))]

        colors = [0,1,2]
        cnt = {}
        for i in colors:
            cnt[i] = nums.count(i)
        
         new_nums = [i for j in [[i] * cnt[i] for i in colors] for i in j]
        
        for i in range(len(nums)):
            nums[i] = new_nums[i]
