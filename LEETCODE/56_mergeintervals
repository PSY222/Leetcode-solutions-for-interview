class Solution:
    def merge(self, intervals):
        res = []
        intervals.sort(key= lambda x: x[0])
        
        if len(intervals) == 1:
            return intervals
        
        for i in intervals:
            if not res or res[-1][1] < i[0]:
                res.append(i)
                
            else:
                res[-1][1] = max(res[-1][1],i[1])
        return res