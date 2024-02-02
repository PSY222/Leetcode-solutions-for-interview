
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        short = min(strs,key = lambda x:len(x))
        ans = ''
        length = 0

        for j in range(len(short)):
            if set([strs[i][length] for i in range(len(strs))]) == set(strs[0][length]):
                ans += strs[0][length]
                length += 1
        return ans
        
#Trie method solution
#source: Leetcode (https://leetcode.com/problems/longest-common-prefix/discuss/1109687/Python-Trie-solution)
# class Solution:
#     def longestCommonPrefix(self, strs: List[str]) -> str:
#         trie = {}
        
#         # Add words to trie
#         for word in strs:
#             curNode = trie
#             for char in word:
#                 if char not in curNode:
#                     curNode[char] = {}
#                 curNode = curNode[char]    
#             curNode['*'] = {}    
        
#         curNode = trie
#         curPre = ''
#         while len(curNode) == 1 and '*' not in curNode: # only have one child and current node is not an endword
#             for key in curNode:
#                 curNode = curNode[key]
#                 curPre += key
#         return curPre        