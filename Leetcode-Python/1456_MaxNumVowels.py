class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        window = s[:k]
        vowels = set(['a', 'e', 'i', 'o', 'u']) 
        cnt = sum(1 for char in window if char in vowels)
        ans = cnt

        for i in range(k, len(s)):
            if s[i - k] in vowels:
                cnt -= 1  
            if s[i] in vowels:
                cnt += 1  
            ans = max(cnt, ans)

            if k == ans:
                return ans

        return ans
