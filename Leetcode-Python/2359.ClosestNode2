class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        n = len(edges)

        def bfs(root, cost):
            q = deque([(root, 0)])
            seen = {root} 
            while q:
                node, step = q.popleft()
                cost[node] = min(cost[node], step) 
                if edges[node] != -1 and edges[node] not in seen:
                    seen.add(edges[node])
                    q.append((edges[node], step + 1))
        # initialise with large number
        cost1 = [inf]*n 
        cost2 = [inf]*n
        bfs(node1, cost1)
        bfs(node2, cost2)
        ans = -1 
        cost = inf
        for i in range(n):
            if cost > max(cost1[i], cost2[i]):
                cost = max(cost1[i], cost2[i])
                ans = i
        return ans