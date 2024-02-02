class Solution:
    def longestPalindrome(self, s:str) -> str:
        res = (0,0)
        for i in range(len(s)):
            b1 = self.expand_pallindrome(s,i,i)  #even
            b2 = self.expand_pallindrome(s,i,i+1) #odd
            res = max(res,b1,b2 key = lambda x : x[1]-x[0]+1)
        return s[res[0]:res[1]]
    
    def expand_pallindrome(self,s,i,j):
        while 0<=i<=j< len(s) and s[i] == s[j]:
            i -= 1
            j += 1
        return (i+1,j)
        
          