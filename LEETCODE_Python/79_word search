class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:                            
        def search(ind,r,c):
            if ind == k:
                return True
            if r>= m or c>=n or r<0 or c<0 :
                return
            tmp = board[r][c]
            if word[ind] != tmp:
                return
            board[r][c] = '#'
            res = search(ind+1,r+1,c) or search(ind+1,r,c+1) or search(ind+1,r-1,c) or search(ind+1,r,c-1)
            board[r][c] = tmp
            return res

        m, n, k = len(board), len(board[0]), len(word)
        tf = []
        for i in [list(set(i)) for i in board]:
            for w in word:
                if w in i: tf.append(True)
        
        if True not in tf:
            return False

        for i in range(m):
            for j in range(n):
                if search(0,i,j):
                    return True
        return False
                