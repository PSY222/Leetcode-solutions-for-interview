class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        ydict = defaultdict(set)
       
        for (x,y) in points:
            ydict[y].add(x)

        ydict = dict(sorted(filter(lambda e: len(list(e[1]))>=2,ydict.items())))
        
        prev_key = next(iter(ydict))
        prev_val = ydict[prev_key]

        ydict.pop(prev_key)
    
        for kys,val in ydict.items():
            common = list(prev_val.intersection(val))
            if len(common) >=2:
                width = common[1]-common[0]
                height = kys - prev_key
                return height*width
            prev = val
            prev_key = kys
        return 0

#Source: https://leetcode.com/problems/minimum-area-rectangle/solutions/515120/python-2-solutions-with-explanation-o-n-2-beats-94/?orderBy=most_votes&languageTags=python
    
def minAreaRect(self, points: List[List[int]]) -> int:
    points.sort()
    points_set = set([tuple(point) for point in points])
    smallest = float('inf')
    for i, (x1, y1) in enumerate(points):
        for j, (x2, y2) in enumerate(points[i:], i):
            if x1 < x2 and y1 < y2 and (x1, y2) in points_set and (x2, y1) in points_set:
                area = (x2 - x1) * (y2 - y1)
                smallest = min(smallest, area)
    return smallest if smallest != float('inf') else 0

        
