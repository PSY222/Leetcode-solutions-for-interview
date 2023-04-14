class Solution:
    def isValid(self, s: str) -> bool:
        dic = {'(':')','{':'}','[':']'}
        stac = []
        for i in s:
            if i in dic:
                stac.append(i)
            elif not stac or dic[stac.pop()] != i:
                return False
            s
        
        return not stac