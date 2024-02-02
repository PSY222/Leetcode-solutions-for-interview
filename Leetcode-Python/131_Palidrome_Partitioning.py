class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        maxp = len(s)

        def test(start,ans):
            if start >= maxp:
                res.append(ans)
            for i in range(maxp-start):
                if s[start:start+i+1] == s[start:start+i+1][::-1]:
                    test(start+i+1,ans+[s[start:start+i+1]])

        
        test(0,[])
        return res

#optimized code that compares palindrome faster

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, part = [], []

        def dfs(i):
            if i >= len(s):
                res.append(part.copy())
                return
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    part.append(s[i : j + 1])
                    dfs(j + 1)
                    part.pop()

        dfs(0)
        return res

    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True       