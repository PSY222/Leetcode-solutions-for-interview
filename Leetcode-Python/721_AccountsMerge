
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        from collections import defaultdict
        visit = [False]*len(accounts)
        emap = defaultdict(list)
        res = []
        
        for i, a in enumerate(accounts):
            for j in range(1,len(a)):
                emap[a[j]].append(i) 
                
    
        def dfs(i,emails):
            if visit[i]:
                return
            visit[i] = True
            for j in range(1,len(accounts[i])):
                email = accounts[i][j]
                emails.add(email)
                for neighbor in emap[email]:
                    dfs(neighbor,emails)
        
        for i, account in enumerate(accounts):
            if visit[i]:
                continue
            name, emails = account[0], set()
            dfs(i,emails)
            res.append([name] + sorted(emails))
        return res
    
        