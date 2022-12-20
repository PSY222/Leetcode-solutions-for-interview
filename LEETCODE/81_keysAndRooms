class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        dic = defaultdict(list)
        
        for v,k in enumerate(rooms):
            dic[v].extend(k)
        
        dq = deque([0])
        visit = set([0])

        while dq:
            curr= dq.popleft()
            for i in dic[curr]:
                if i not in visit:
                    dq.append(i)
                    visit.add(i)       
        return len(list(visit)) == len(rooms)