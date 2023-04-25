# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        dq = deque([(0,root)])
        currmax = 0
        while dq:
            level_idx = []
            for _ in range(len(dq)):
                id, node = dq.popleft()
                level_idx.append(id)
                if node.left:
                    dq.append((2*id+1,node.left))
                if node.right:
                    dq.append((2*id+2,node.right))
            currmax = max(currmax,level_idx[-1]-level_idx[0]+1)
        return currmax
                
            
        