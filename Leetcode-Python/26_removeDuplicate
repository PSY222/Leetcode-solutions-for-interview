class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 1
        length = len(nums)
        for i in range(1,length):
            if nums[i-1] != nums[i]:
                nums[idx] = nums[i]
                idx += 1
        return idx
                