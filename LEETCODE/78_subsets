from itertools import combinations
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #[] empty list should also be included
        #all the combinations - duplicates included
        
        #iterative method(1,2,3) using itertools
        # res = []
        # for i in range(1,len(nums)+1):
        #     res.extend(itertools.combinations(nums,i))
        # res.append([])
        # return res
        
        res = [[]]
        def btrack(c,cur,i):
            if len(cur) == c:
                res.append(list(cur))
                return
            if i >= len(nums):
                return
            #for i in range(len(nums)):
            cur.append(nums[i])
            btrack(c,cur,i+1)
            cur.pop()
            btrack(c,cur,i+1)
                
            
        for i in range(1,len(nums)+1):
            btrack(i,[],0)
        return res
            
                        
                
                    
    
    