class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        begin, end = 0, len(str_x)-1
        ans = True
        
        while 0<=begin<end:
            if str_x[begin] != str_x[end]:
                ans = False
                break
            begin += 1
            end -= 1
        return ans