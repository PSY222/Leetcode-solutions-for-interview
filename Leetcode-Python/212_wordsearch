class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        m, n = len(board), len(board[0])
        visit = [[False]*n for i in range(m)]
        
        def dfs(wrd,r,c):
            if len(wrd) == 0:
                return True
            visit[r][c] = True
            steps = [0,1,0,-1,0]
            for s in range(len(steps)-1):
                new_r = steps[s] + r
                new_c = steps[s+1] + c
                if 0<= new_r <m and 0<=new_c<n and not visit[new_r][new_c] and board[new_r][new_c] == wrd[0]:
                    if dfs(wrd[1:],new_r,new_c):
                        visit[new_r][new_c] =False
                        return True
            visit[new_r][new_c] = False
            return False
       
        res = []
        for word in words:
            wasfound = False
            for i in range(m):
                for j in range(n):
                    if board[i][j] == word[0]:
                        if dfs(word[1:],i,j) and word not in res:
                            res.append(word)
                            wasfound = True
                            break
                if wasfound:
                    break

        return res