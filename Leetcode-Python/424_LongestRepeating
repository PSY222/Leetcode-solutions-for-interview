class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i = res = 0
        cnt = defaultdict(int)
        for n in range(len(s)):
            cnt[s[n]] += 1
            curr_len = n-i+1
            if curr_len -max(cnt.values()) > k:
                cnt[s[n]] -= 1
                i += 1
            else:
                res = max(res,curr_len)
        return res
            
            