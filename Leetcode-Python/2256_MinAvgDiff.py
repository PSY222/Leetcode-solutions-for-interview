class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        left, right = 0, sum(nums)
        ans = {}
        
        for i in range(len(nums)):
            left += nums[i]
            right -= nums[i]
            try:
                mad = abs(left//(i+1) -right//(len(nums)-1-i))
            except:
                mad = left//(i+1)             
            # if list(ans.items())[-1][1] > mad:
            #     ans.popitem()   # To add the memory usage efficiency, we can filter the elements before adding to a dictionary
            ans[i] = mad
        return min(ans.items(),key= lambda x: x[1])[0]
        #return list(ans.keys())[0]