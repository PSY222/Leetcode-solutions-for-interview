import heapq
import numpy as np

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        dist = {i:abs(j) for i,j in zip(arr,arr-np.full(len(arr),x))}
        pairs = sorted(dist.items(),key=lambda x:x[1])
        
        return sorted([i[0] for i in pairs][:k])  