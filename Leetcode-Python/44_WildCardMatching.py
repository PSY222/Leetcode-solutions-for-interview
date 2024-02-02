#1. DFS Method (Source:https://leetcode.com/problems/wildcard-matching/discuss/1336621/Python-DFS-with-Memoization-Clean-and-Concise)

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(None)
        def dfs(i, j):
            if j == len(p):  # Reach full pattern
                return i == len(s)

            if i < len(s) and (s[i] == p[j] or p[j] == '?'): 
                return dfs(i + 1, j + 1)
            
            if p[j] == '*':
                return dfs(i, j + 1) or i < len(s) and dfs(i + 1, j)  # Match zero or one or more character
            
            return False

        return dfs(0, 0)


#2. Dynamic Programming

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False]*(len(p)+1) for _ in range(len(s)+1)]
        dp[0][0] = True
        
        for j in range(1,len(p)+1):
            if p[j-1] != '*':
                break
            dp[0][j] = True
            
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1] == '?' or s[i-1] == p[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                elif p [j-1] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
        return dp[-1][-1]


#3. Two Pointer(https://leetcode.com/problems/wildcard-matching/discuss/1365119/No-dp-oror-60-ms-faster-than-87.73-of-Python3-Double-pointer-question)

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = j = 0  
        back_j = -1  
        match_i = 0   
        m = len(s)
        n = len(p)
        while i < m:
            if j < n and (s[i] == p[j] or p[j] == '?'):  
                i += 1
                j += 1
            elif j < n and p[j] == '*':  
                back_j = j  
                match_i = i  
                j += 1  
            elif back_j != -1:  
                j = back_j + 1
                match_i += 1  
                i = match_i
            else:  
                return False
            print(p[j:])
        return list(p[j:]).count('*') == len(p[j:]) 