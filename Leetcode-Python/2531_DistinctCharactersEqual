#Wrong solution
class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        c1 = {j:i for i, j in Counter(word1).items()}
        del c1[1]
        c2 = {j:i for i, j in Counter(word2).items()}
        del c2[1]
        
        swap = set(c1.values())-set(c2.values()) or set(c2.values())-set(c1.values())
        val = swap.pop()
        
        if len(c1)==0 or len(c2)==0:
                    return False
        return True  
        
#Leetcode discussion example 
    a,b = Counter(word1),Counter(word2) 
    c,d = a.copy(),b.copy()
    for i in a: 
        for j in b: 
            c[i], c[j], d[j], d[i] = c[i]-1, c[j]+1, d[j]-1, d[i]+1
            if not c[i]: del c[i] 
            if not d[j]: del d[j] 
            if len(c)==len(d): return True #after swap 
            c,d = a.copy(),b.copy() 
    return False