class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        ans = 0
        vals = Counter(tasks).values()
        for j in vals:
            if j ==1:
                return -1
            ans += (j+2)//3
        return ans