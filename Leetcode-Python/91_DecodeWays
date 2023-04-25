class Solution:
    def numDecodings(self, s: str) -> int:
        #This question is similar to climbing stairs DP problem
        # Source: https://leetcode.com/problems/decode-ways/discuss/1029225/Simple-and-detail-solution-with-explanation
        dp = [0]*(len(s)+1)
        dp[0],dp[1] = 1,1
        
        if s[0] == '0':
            return 0
        
        for i in range(2,len(s)+1):
            if 1 <= int(s[i-1]) <= 9:  #Or we can just check int(s[i-1]) != 0
                dp[i] += dp[i-1]
            if 10 <= int(s[i-2] +s[i-1]) <= 26:
                dp[i] += dp[i-2]
            return dp[-1]

#Otherwise, we can use dynamic programming with dfs approach
#Source: https://leetcode.com/problems/decode-ways/discuss/608268/Python-Thinking-process-diagram-(DP-%2B-DFS)

class Solution:
    def numDecodings(self, s:str) -> int:
        if len(s) == 0 or s is None:
            return 0

        @lru_cache(maxsize=None)
        def dfs(string):
            if len(string)>0:
                if string[0] == '0':
                    return 0
            if string == "" or len(string) == 1:
                return 1
            if int(string[0:2]) <= 26:
                first = dfs(string[1:])
                second = dfs(string[2:])
                return first+second
            else:
                return dfs(string[1:])

        result_sum = dfs(s)

        return result_sum