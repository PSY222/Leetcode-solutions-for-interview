class Solution:
    def shortestPalindrome(self, s: str) -> str:

        def isvalid(val):
            return True if val == val[::-1] else False

        l, r= 0, len(s)
        cnt = 0
        while not isvalid(s[l:r]):
            r -= 1
            cnt += 1

        return s[-cnt:][::-1] + s if cnt != 0 else s

            
#Similar short solution
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        for i in range(len(s)-1,-1,-1):
            a = s[:i+1]
            b = a[::-1]
            if a==b:
                c = s[i+1:]
                c = c[::-1]
                return c+a+c[::-1]
        s1 = s[1:]
        return s1[::-1] + s