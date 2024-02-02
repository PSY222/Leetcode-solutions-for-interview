class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)
        c2 = Counter(word2)
        a, b = sorted(c1.values()), sorted(c2.values())
        return c1.keys() == c2.keys() and a ==b