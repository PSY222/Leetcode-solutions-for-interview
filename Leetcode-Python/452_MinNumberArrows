class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points,key=lambda x:(x[0],x[1]))
        start = points[0][1]
        ans = 1
        for i in points:
            if i[0] > start:
                ans +=1
                start = i[1]
            if i[1] < start:
                start = i[1]
        return ans
            