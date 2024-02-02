class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []       
        in_degree = defaultdict(int)
        out_degree = defaultdict(list)
        
        if prerequisites == []:
            return range(numCourses)
        
        for i in prerequisites:
            in_degree[i[0]] += 1
            out_degree[i[1]].append(i[0])
        
        start,visit = [k for k in range(numCourses) if not in_degree[k]], set()
        
        while start:
            curr = start.pop()
            res.append(curr)
            if curr in visit:
                continue
            visit.add(curr)
            
            
            for od in out_degree[curr]:
                in_degree[od] -= 1
                if not in_degree[od]:
                    start.append(od)
                
        return res if len(res) == numCourses else []