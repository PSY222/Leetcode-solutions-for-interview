class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res, size = [], len(p)
        
        def find(word,p,i):
            if i >= len(s)-size:
                return res
            if sorted(word) == sorted(p):
                res.append(i)
            word = word.replace(s[i],s[i+size])
            find(word,p,i)
        
        for i in range(len(s)-size):
                find(s[:size],p,i)
                
        return res
                
            
        
        #brute force approach
#         def dfs(s,p,i):
#             if i > len(s):
#                 return res
#             if sorted(p) == sorted(s[i:i+len(p)]):
#                 res.append(i)
        
#         for i in range(len(s)-len(p)+1):
#             if s[i] in p:
#                 dfs(s,p,i)
#         return res