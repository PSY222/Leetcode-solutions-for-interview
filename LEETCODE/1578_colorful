class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
            res = []
            start, end = 0, 1
            
            if len(colors) == len(list(set(colors))):
                return 0
            
            def detect(start,end,colors):
                while start < end < len(colors):
                    if colors[start] == colors[end]:
                        detect(start,end + 1,colors)
                    else:
                        res.append(min(neededTime[start:end+1]))
                        detect(end,end+1,colors)
                return res
            return detect(start,end,colors)