class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        one, ans = 0, 0

        for i in s:
            if i=='1':
                one += 1
            elif one:
                one -= 1
                ans +=1
        return ans