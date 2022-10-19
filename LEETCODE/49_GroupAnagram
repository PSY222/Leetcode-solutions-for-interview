class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        
        if len(strs) == 1:
            return [strs]
        
        for i in strs:
            res[''.join(sorted(i))].append(''.join(i))
        return res.values()