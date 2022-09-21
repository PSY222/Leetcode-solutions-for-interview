class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        
        if len(nums) <= 1 or not nums:
            return []
        
        for k, val in enumerate(nums[:-2]):
            i = k + 1
            j = len(nums)-1
            
            while i < j :
                i_num, j_num = nums[i], nums[j]
                total = i_num + j_num + val
                if total == 0:
                    if [i_num,j_num,val] not in answer:
                        answer.append([i_num,j_num,val])
                    i += 1
                    j -= 1
                    
                elif total > 0:
                    j -= 1
                    
                elif total < -val:
                    i += 1
                        
                
        return answer