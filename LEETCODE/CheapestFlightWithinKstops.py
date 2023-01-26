#BFS method
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dic = defaultdict(list)
        dp = [-1 for _ in range(n)]

        for i in flights:
            s,d,p = i
            dic[s].append([d,p])

        q = deque([src])
        while q and k>=0:
            new = list(dp)
            for _ in range(len(q)):
                cur = q.popleft()
                for neigh in dic[cur]:
                    if new[neigh[0]] == -1 or new[neigh[0]] > dp[cur] + neigh[1]:
                        new[neigh[0]] = dp[cur] + neigh[1]
                        q.append(neigh[0])
            k -= 1
            dp = new
    
        return dp[dst]+1 if dp[dst] != -1 else -1

 #Bellma ford algo from LeetCode
    def findCheapestPriceBellManFord(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
       
        costs = [float("inf")] * n

        costs[src] = 0
        for i in range(k + 1):
            temp = costs.copy()
            for start, end, price in flights:
                if costs[start] != float("inf"):
                    temp[end] = min(costs[start] + price, temp[end])
            costs = temp
        return costs[dst] if costs[dst] != float("inf") else -1