class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None: 
        def divide(arr,low,high):
            piv = arr[high]
            i = low-1
            for j in range(low,high):
                if arr[j] <= piv:
                    i = i+1
                    (arr[i], arr[j]) = (arr[j], arr[i])
            (arr[i+1], arr[high]) = (arr[high], arr[i+1])
            return i+1
        
        def quicksort(arr,low,high):
            if low < high:
                pr = divide(arr,low,high)
                divide(arr,low,pr-1)
                divide(arr,pr+1,high)
            return arr
        
        if n == 0: return nums1
        
        for l in range(m+n-1,m-1,-1):
            nums1[l] = nums2.pop()

        return quicksort(nums1,0,m+n-1)
    
    #Source: https://leetcode.com/problems/merge-sorted-array/discuss/29503/Beautiful-Python-Solution
        # while n >0 :
        #     if m <= 0 or nums2[n-1] >= nums1[m-1]:
        #         nums1[m+n-1] = nums2[n-1]
        #         n -=1
        #     else:
        #         nums1[m+n-1] = nums1[m-1]
        #         m -= 1
