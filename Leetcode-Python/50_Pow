class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
             return 1
        if n < 0:
             x = 1/x
             n = -n
        return self.myPow(x*x,n//2) if n%2==0 else x*self.myPow(x*x,n//2)


# Source: https://leetcode.com/problems/powx-n/discuss/738830/Python-recursive-O(log-n)-solution-explained
#Faster solution

class Solution:
    def myPow(self, x, n):
        if abs(x) < 1e-40: return 0 
        if n == 0: return 1
        if n < 0: return self.myPow(1/x, -n)
        
        lower = self.myPow(x, n//2)
        if n % 2 == 0: return lower*lower
        if n % 2 == 1: return lower*lower*x