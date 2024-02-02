class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        record = defaultdict(list)
        calc = defaultdict(int)
        for i in range(len(creators)):
            record[creators[i]].append((views[i],ids[i]))
            calc[creators[i]] += views[i]
            
        names = sorted(list(calc.items()),key = lambda x: x[1],reverse=True)
        max_val = names[0][1]
        res = []
        del calc
        
        for n, v in names:
            if v != max_val:
                break
            vid = sorted(list(record[n]),key = lambda x:x[0],reverse=True)
            max_vv = vid[0][0]
            ids = []
            for a,b in vid:
                if a != max_vv:
                    break
                ids.append(b)
            res.append([n,min(ids)])
        return res
        