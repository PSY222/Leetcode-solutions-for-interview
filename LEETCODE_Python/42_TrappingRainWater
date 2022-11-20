class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)==1:
            return 0
        
        res = 0
        ml = mr = 0
        start, end = 0, len(height)-1
        
        while end > start:
            if height[start] < height[end]:
                if height[start] > ml:
                    ml = height[start]
                else:
                    res += (ml-height[start])
                start += 1
            else:
                if height[end] > mr:
                    mr = height[end]
                else:
                    res += (mr-height[end])
                end -= 1
        return res
                
            
        