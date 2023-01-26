class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = []

        def combs(idx,path):
            if len(path) >= 2:
                res.append(path)
            visit = set()
            for i in range(idx+1, len(nums)):
                if nums[i] >= nums[idx] and nums[i] not in visit:
                    combs(i,path+[nums[i]])
                visit.add(nums[i])
            return

        check = set()
        for i in range(len(nums)):
            if nums[i] not in check:
                combs(i,[nums[i]])
            check.add(nums[i])
        return res

        