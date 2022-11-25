#TLE solution
class Solution1:
    def climbStairs(self, n: int) -> int:
        steps = [1,2]

        def find(n,path,res):
            if n < 0:
                return
            if n == 0:
                res.append(path)
            for i in steps:
                find(n-i,path+[i],res)
        
        res = []
        find(n,[],res)
        return len(res)

#dict type memoization
class Solution2:
    def climbStairs(self, n: int) -> int:
        dic = {1:1,2:2}
        def find(n):
            if n in dic:
                return dic[n]
            else:
                dic[n] = find(n-1) + find(n-2)
                return dic[n]
        return find(n)