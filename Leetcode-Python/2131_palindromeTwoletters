class Solution:
    def longestPalindrome(self, words: List[str]) -> int:

        match = Counter(words)
        ans, rest = 0, 0
        for i in match:
            if i == i[::-1]:
                ans += (match[i]//2)*4
                rest = max(rest,(match[i]%2)*2)
            elif i[::-1] in match:
                ans += (min(match[i],match[i[::-1]]))*2
                
        return ans + rest