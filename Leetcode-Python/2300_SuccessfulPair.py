class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans = []
        potions.sort()  
        
        for s in spells:
            length = len(potions)
            left, right = 0, length - 1
            count = 0 
            
            while left <= right:
                mid = left + (right - left) // 2
                if s * potions[mid] >= success:
                    right = mid - 1
                    count = length - mid  
                else:
                    left = mid + 1
            
            ans.append(count)  
        
        return ans
