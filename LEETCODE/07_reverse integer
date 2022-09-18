class Solution:
    def reverse(self, x: int) -> int:
        
        if x>= 0:
            answer = int(''.join([i for i in str(x)][::-1]))
        
        elif x <= 0:
            answer = int(''.join([i for i in str(x)][::-1][:-1]))*(-1)
        
        return answer if pow(-2,31) < answer < pow(2,31) else 0