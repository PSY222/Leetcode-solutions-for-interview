
class Solution:
    def myAtoi(self, s: str) -> int:
        ans, sig = '', 1
        front_num = False
        mark = ['+','-']
        
        if len(s) == 1 and s[0] in mark:
            return 0
        
            
        for idx, i in enumerate((s.strip(' ')).split(' ')[0]):
            if i.isalpha():
                break
            if i == '-' and front_num == False:
                sig = -1
            if i.isdigit() or (i =='.' and front_num):
                ans += i
                front_num = True
            if (front_num and i.isdigit() == False) or (s[idx] in mark and s[idx+1] in mark) or (i =='.' and front_num == False):
                break

        return min(2**31,floor(float(ans)))*(-1) if ans != '' and sig < 0 else min(2**31-1,floor(float(ans))) if ans != '' and sig > 0 else 0
