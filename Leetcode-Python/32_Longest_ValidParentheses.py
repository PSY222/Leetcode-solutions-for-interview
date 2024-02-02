class Solution:
    def longestValidParentheses(self, s: str) -> int:
        curr = maxL = 0
        stac = [-1]
        for i in range(len(s)):
            if s[i] == '(':
                stac.append(i)
            else:
                stac.pop()
                if not stac:
                    stac.append(i)
                else:
                    maxL = max(maxL,i-stac[-1])
        return maxL