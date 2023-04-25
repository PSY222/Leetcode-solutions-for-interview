class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        base =[a-b for a,b in zip(capacity,rocks) if a-b != 0]
        base.sort()
        ans = len(capacity) - len(base)
        for i in base:
            additionalRocks -= i
            if additionalRocks < 0:
                break
            else:
                ans += 1
        return ans
