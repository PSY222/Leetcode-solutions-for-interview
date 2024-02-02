        def dfs(limit,r,c):
            if r==limit or c == limit:
                return True
            visit[r][c] == 0
            for add_r,add_c in steps:
                new_r = add_r + r
                new_c = add_c + c
                if new_r>len(heights) or new_c>len(heights[0]) or new_r <0 or new_c<0:
                    continue
                if heights[new_r][new_c] > heights[r][c]:
                    continue
                dfs(limit,new_r,new_c)
                    
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if all([dfs(0,r,c),dfs(len(heights[0]),r,c),visit[r][c] == 1]):
                    res.append([r,c])
        return res