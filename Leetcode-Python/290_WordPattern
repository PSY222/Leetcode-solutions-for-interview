class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        slist = s.split(' ')

        if len(Counter(pattern)) != len(Counter(slist)) or len(pattern) != len(slist):
            return False

        dic = defaultdict(set)
        for p,sv in zip(pattern,slist):
            if not dic[p]:
                dic[p] = sv
            elif dic[p] != sv:
                return False
        return True