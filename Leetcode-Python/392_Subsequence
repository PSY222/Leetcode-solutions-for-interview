    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        
        leftS = 0
        for i in t:
            if s[leftS] == i:
                leftS += 1
                if leftS == len(s):
                    return True
        
        return False
