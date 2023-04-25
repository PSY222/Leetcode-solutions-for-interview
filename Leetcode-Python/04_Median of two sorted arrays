import numpy as np
from bisect import insort
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        longer = nums1 if len(nums1) >= len(nums2) else nums2
        shorter = nums1 if len(nums1) < len(nums2) else nums2
        
        while shorter:
            insort(longer,shorter.pop(),0,len(longer))
        return np.median(longer)

#binary search
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a, b = nums1, nums2
        total = len(a) + len(b)
        half = total // 2 
        if len(a) > len(b): 
            a, b =b, a
        l=0
        r= len(a)-1
        while True: 
            i=(l+r)//2
            j=half-i-2

            aLeft=a[i] if i>=0 else float('-infinity')
            aRight=a[i+1] if i+1 < len(a) else float('infinity')
            bLeft=b[j] if j>=0 else float('-infinity')
            bRight=b[j+1] if j+1 < len(b) else float('infinity')

            if aLeft <= bRight and bLeft <= aRight: 
                if total % 2: 
                    return min(aRight, bRight)
                else: 
                    return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
            elif aLeft > bRight: 
                r = i - 1
            else: 
                l = i + 1


#My solution using heapq
import heapq

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = len(nums1) + len(nums2)
        median_loc = [length // 2+1, length // 2] if length % 2 == 0 else [length // 2+1]
        combined = nums1 + nums2
        heapq.heapify(combined)
        
        if len(median_loc) == 1:
            idx = median_loc.pop()
            return heapq.nsmallest(idx, combined)[-1]
        else:
            first = median_loc.pop()
            second = median_loc.pop()
            return sum(heapq.nsmallest(second, combined)[first-1:second+1]) / 2


                    