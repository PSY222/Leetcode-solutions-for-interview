#Source: https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/28917/AC-Python-clean-solution-using-stack-76ms
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:        
        heights.append(0)  
        stack = [-1]
        ans = 0
        
        for i in range(len(heights)):
            while heights[i] <heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i - stack[-1] -1
                ans = max(ans,h*w)
            stack.append(i)
        heights.pop()
        return ans

#Source: https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/510500/python-using-stack
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = []
        heights = [0] + heights + [0]
        for i in range(len(heights)):
            while(stack and heights[stack[-1]] > heights[i]):
                j = stack.pop()
                ans = max(ans, (i-stack[-1]-1)*heights[j])
            stack.append(i)
        return ans