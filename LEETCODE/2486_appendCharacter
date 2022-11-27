class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        ans = len(t)
        val = 0
        for i in s:
            if i == t[val]:
                val += 1
            if val > ans-1:
                break
        return ans -val