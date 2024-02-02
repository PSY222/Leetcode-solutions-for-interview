class Solution1:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root,float('-inf'))]
        count = 0
        while stack:
            node, maxNum = stack.pop()
            if node.val>=maxNum:
                count+=1
            maxNum = max(maxNum,node.val)
            if node.left:
                stack.append((node.left,maxNum))
            if node.right:
                stack.append((node.right,maxNum))
        return count
    
class Solution2:
    def goodNodes(self, root: TreeNode) -> int:
        return self.checkNodes(root, root.val)
    
    def checkNodes(self, root, n):
        count = 0
        if not root:
            return 0
        if n <= root.val:
            count += 1
        
        newMax = max(n, root.val)
        return count + self.checkNodes(root.left, newMax) + self.checkNodes(root.right, newMax)