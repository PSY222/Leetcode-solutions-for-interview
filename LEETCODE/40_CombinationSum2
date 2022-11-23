class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        self.comb(sorted(candidates),target,[],res)
        return res
    
    def comb(self,cand,target,path,res):
        if target < 0:
            return
        if target == 0:
                res.append(path)
        for i in range(len(cand)):
            if i >0 and cand[i] == cand[i-1]:          #How to avoid duplicates
                continue
            if cand[i] > target:           #backtracking, avoid unnecessary calculations
                break
            self.comb(cand[i+1:],target-cand[i],path+[cand[i]],res)