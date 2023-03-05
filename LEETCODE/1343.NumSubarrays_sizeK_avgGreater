class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        start = sum(arr[0:k])
        ans = 1 if start//k >= threshold else 0
        
        for i in range(len(arr)):
            if k +i < len(arr):
                total = (start-arr[i]+arr[k+i])
                if  total >= threshold*k:
                    ans += 1
                start = total
        return ans