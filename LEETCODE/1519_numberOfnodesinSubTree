#Misinterpreted question
#Always read the question carefully! It is undirected graph
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        dicA = dict()
        dicB = defaultdict(list)

        for i,j in zip(range(n),labels):
            dicA[i] = j #number: label

        for m,n in edges:
            dicB[m].append(n)  #number: neighbors

        def dfs(val,res):
            stac=[val]
            visit =set()
            while stac:
                node = stac.pop()
                if node not in visit:
                    visit.add(node)
                    for i in dicB[node]:
                        stac.append(i)
                        if dicA[i] == dicA[val]:
                            res += 1  
            return res

        ans = []
        for i in range(n):
           ans.append(dfs(i,1))

        return ans

#Proper solution(Considered undirected graph)
#source: https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/solutions/3037908/python-3-11-lines-recursion-w-explanation-t-m-100-95/
class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph, labelCnt, ans = defaultdict(list), defaultdict(int), [0] * n
        
        for a, b in edges:                              
            graph[a].append(b) #make a dictionary with the connection btw nodes
            graph[b].append(a)
        
        def dfs(node=0, par=None):                      
            prev = labelCnt[labels[node]]
            labelCnt[labels[node]] += 1
            
            for child in graph[node]:
                if child != par: dfs(child, node)

            ans[node] = labelCnt[labels[node]] - prev  

        dfs()
        return ans        