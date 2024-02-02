class Solution:
    def simplifyPath(self, path: str) -> str:
        splitPath = [i for i in path.split('/') if i !='']
        ans = []
        for p in splitPath:
            if p.isalpha():
                ans.append(p)
            elif p =='..':
                if ans != []:
                    ans.pop()
            elif p =='.':
                pass
            else:
                ans.append(p)
        return '/'+'/'.join(ans)



# class Solution:
#     def simplifyPath(self, path: str) -> str:
#         ans = []
#         word = ''
#         idx = 0
#         for i in range(len(path)-1,0,-1):
#             if path[i].isalpha():
#                 idx = i
#                 break
        
#         path = path[:idx+1]+'/'
  
#         prev = path[0]
#         for p in path[1:]:
#             if p.isalpha():
#                 word += p
#             if p =='.' and len(ans)!=0:
#                 ans =[]
#             if prev.isalpha() and p =='/':
#                 ans.append(p)
#                 ans.append(word)
#                 word = ''
#             prev = p
#         return ''.join(ans) if ans else '/'