#TLE => Minimize the repeated computation, think about other methods like hashmap

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = set()
        word_dic = Counter(words)
        wl = len(words[0])
        
        def repeat(i):
            remain = word_dic.copy()
            used = 0
            
            for j in range(i,i+wl*len(words),wl):
                chunk = s[j:j+wl]
                if remain[chunk] > 0:
                    remain[chunk] -= 1
                    used += 1
                else:
                    break
            return used == len(words)
            
        for i in range(len(s)-wl*len(words)+1):
            if repeat(i):
                res.add(i)
                
        return res