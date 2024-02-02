class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        indegree, neighbor = defaultdict(int), defaultdict(list)
        
        for e in edges:
            indegree[e[0]] += 1
            indegree[e[1]] += 1
            neighbor[e[1]].append(e[0])
            neighbor[e[0]].append(e[1])

        start, visit = [i for i in range(n) if indegree[i] == max(indegree.values())], set()
        
        while start:
            node = start.pop()
            if node not in visit:
                visit.add(node)
                for neigh in neighbor[node]:
                    indegree[neigh] -= 1
                    if indegree[neigh] > 0:
                        start.append(neigh)
        return visit