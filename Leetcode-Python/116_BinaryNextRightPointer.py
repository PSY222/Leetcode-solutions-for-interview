"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
#Source : https://leetcode.com/problems/populating-next-right-pointers-in-each-node/solutions/37484/7-lines-iterative-real-o-1-space/

def connect(self, root):
    while root and root.left:
        next = root.left
        while root:
            root.left.next = root.right
            root.right.next = root.next and root.next.left
            root = root.next
        root = next
    return root

#Source: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/solutions/37715/python-solutions-recursively-bfs-queue-dfs-stack/
#Recursive
def connect1(self, root):
    if root and root.left and root.right:
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
 
# BFS       
def connect2(self, root):
    if not root:
        return 
    queue = [root]
    while queue:
        curr = queue.pop(0)
        if curr.left and curr.right:
            curr.left.next = curr.right
            if curr.next:
                curr.right.next = curr.next.left
            queue.append(curr.left)
            queue.append(curr.right)
    return root
    
# DFS 
def connect(self, root):
    if not root:
        return 
    stack = [root]
    while stack:
        curr = stack.pop()
        if curr.left and curr.right:
            curr.left.next = curr.right
            if curr.next:
                curr.right.next = curr.next.left
            stack.append(curr.right)
            stack.append(curr.left)
    return root

#Leetcode top solution: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/submissions/855389927/
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root or not root.right or not root.left:
            return root
        
        self.connectNodes(root, None)
        return root
    
    def connectNodes(self, root, nxt):
        if not root:
            return
        
        root.next = nxt
        self.connectNodes(root.left, root.right)
        self.connectNodes(root.right, root.next.left if root.next else None)

