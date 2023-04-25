class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        maps = defaultdict(list)

        for (i,j) in zip(s,t):
            if not maps[i] and j not in maps.values():
                maps[i] = j
            elif maps[i] != j:
                return False
        return True

#Very simple and smart solution
class Solution:
    def isIsomorphic(self, a: str, b: str) -> bool:
        return len(set(a)) == len(set(b)) == len(set(zip(a,b)))