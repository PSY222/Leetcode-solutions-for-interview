class Solution1:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return []
        dic={'2':['a','b','c'], '3':['d','e','f'], '4':['g','h','i'], '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}
        res=[]
        n=len(digits)
        def backtracking(r):
            if len(r)==n:
                res.append(r)
            else:
                for i in dic[digits[len(r)]]:
                    backtracking(r+i)
        backtracking("")            
        return res
    
class Solution2:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == '':
            return ''
        letters = {"2":"abc",
                    "3":"def",
                    "4":"ghi",
                    "5":"jkl",
                    "6":"mno",
                    "7":"pqrs",
                    "8":"tuv",
                    "9":"wxyz"}
        output = []

        def backtrack(combination, nextdigits):
            if len(nextdigits) == 0:
                output.append(combination)
            else:
                for c in letters[nextdigits[0]]:
                    backtrack(combination + c , nextdigits[1:])
        backtrack("",digits)
        return output
