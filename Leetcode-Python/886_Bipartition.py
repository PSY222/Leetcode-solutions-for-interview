class Solution(object):
    def possibleBipartition(self, n, dislikes):
        conn = defaultdict(set)
        colors = [-1]*(n+1)

        for (a,b) in dislikes:
            conn[a].add(b)
            conn[b].add(a)
        
        def bfs(i):
            dq = deque([i])
            colors[i] = 0
            while dq:
                curr = dq.popleft()
                for neigh in conn[curr]:
                    if colors[curr] == colors[neigh]:
                        return False
                    if colors[neigh] == -1:
                        colors[neigh] = 1-colors[curr]
                        dq.append(neigh)
            return True

        for i in range(1,n+1):
            if colors[i] == -1:
                if not bfs(i):
                    return False
        return True