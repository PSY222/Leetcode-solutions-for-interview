class Solution1:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return max(left_depth, right_depth) + 1
    
class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        queue = [(root, 1)]
        max_depth = 0
        
        while queue:
            node, depth = queue.pop(0)
            max_depth = max(max_depth, depth)

            if node.left:
                queue.append((node.left, depth+1))

            if node.right:
                queue.append((node.right, depth+1))
        return max_depth