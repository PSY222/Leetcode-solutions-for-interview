class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s , e = newInterval
        l, r = [], []
        
        for i in intervals:
            if i[1] < s:
                l.append(i)
            elif i[0] > e:
                r.append(i)
            else:
                s = min(s,i[0])
                e = max(e,i[1])
        
        return l+[[s,e]]+r

#Another solution
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        loc = bisect_left(intervals,newInterval)
        intervals.insert(loc,newInterval)

        i = 1
        while i < len(intervals):
            s, e = intervals[i]
            if intervls[i-1][1] >= s:
                prevS, prevE = intervals[i-1]
                intervlas[i-1:i+1] = [[prevS,max(prevE,e)]]
            else:
                i += 1
        return intervals
                
                
            