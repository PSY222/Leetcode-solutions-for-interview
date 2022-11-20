class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        
        x = self.countAndSay(n-1)
        res, val, cnt = '', x[0],1
        
        for i in range(1,len(x)):
            if x[i] == val:
                cnt += 1
            else:
                res += str(cnt) + val
                val, cnt = x[i], 1
        res += str(cnt) + val
        return res