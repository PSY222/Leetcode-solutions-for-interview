class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        dic = defaultdict(list)
        ans = False
        for e in edges:
            dic[e[0]].append(e[1])
            dic[e[1]].append(e[0])

        stac =[source]
        visit = set()
        while stac :
            curr = stac.pop()
            if curr == destination:
                return True
            for conn in dic[curr]:
                if conn not in visit:
                    stac.append(conn)
                    visit.add(conn)
        return ans