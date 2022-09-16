class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = []
        length = []
        
        for i in s:
            if i not in temp:
                temp.append(i)
            else:
                length.append(len(temp))
                temp = []
                temp.append(i)
                
        length.append(len(temp))      
        return max(length, default = 1) if s != "" else 0
