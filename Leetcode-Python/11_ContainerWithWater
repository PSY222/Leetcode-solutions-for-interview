class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        ans = 0
        while left < right:
            h_left, h_right = height[left], height[right]
            width = right - left
            area = min(h_left, h_right) * width
            ans = max(area, ans)

            if h_left < h_right:
                left += 1
            else:
                right -= 1
            
        return ans