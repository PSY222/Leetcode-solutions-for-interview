#two pointers solution
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        s = s.lower()
        while (l < r):
            if not s[l].isalnum():
                l += 1
            elif not s[r].isalnum():
                r -= 1
            elif s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1

        return True
    
#Simple comparison using [::-1]
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s)).lower()

        return s == s[::-1]