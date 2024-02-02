class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = collections.defaultdict(set)
        adj_dict = collections.defaultdict(set)
        
        for a,b in prerequisites:
            indegree[a].add(b)
            adj_dict[b].add(a)
        
        start = [i for i in range(numCourses) if not indegree[i]]
        visit = collections.deque()
        
        while start:
            s = start.pop()
            visit.append(s)
            
            for a in adj_dict[s]:
                indegree[a].remove(s)
                if not indegree[a]:
                    start.append(a)
                
        return len(visit) == numCourses