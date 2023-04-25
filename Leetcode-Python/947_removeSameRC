class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        connect = defaultdict(set)        
        for idx, s in enumerate(stones):
            for cn, j in enumerate(stones):
                if (s[0] == j[0] or s[1] == j[1]) and s !=j:
                    connect[idx].add(cn)
        
        cnt = 0
        visit = set()
        for i in range(len(stones)):
            if self.dfs(connect,i,visit):
                cnt += 1
        return len(stones) - cnt
    
    def dfs(self,connect,curr,visit):
        if curr in visit:
            return False
        visit.add(curr)
        for neigh in connect[curr]:
            self.dfs(connect,neigh,visit)
        return True
        