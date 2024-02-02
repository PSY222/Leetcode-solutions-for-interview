class Solution1:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for i in asteroids:
            while s and i < 0 < (b := s[-1]):
                if b <= -i : s.pop()
                if b >= -i : break
            else:
                s.append(i)
        return s
    
class Solution2:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for el in asteroids:
            while res and el < 0 < res[-1]:
                if abs(el)>abs(res[-1]):
                    res.pop()
                    continue
                elif abs(el)==abs(res[-1]):
                    res.pop()
                break
            else:
                res.append(el)
        return res
                
                
 