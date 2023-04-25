import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hp, dist = [], lambda x, y : x**2 + y**2
        
        for i in points:
            x, y = i
            d = dist(x,y)
            
            if len(hp) == k:
                heapq.heappushpop(hp,(-d,i))
                
            else:
                heapq.heappush(hp,(-d,i))
                
        return [i[1] for i in hp]