# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #DFS
        """
        if not root:
            return 0
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        
        if not left or not right:
            return 1 + left + right
        else:
            return 1 + min(left,right)
        """
        #BFS
        if not root:
            return 0
        ans = 99999
        queue = [(root,1)]
        while queue:
            node,depth = queue.pop(0)
            if node and not node.left and not node.right:
                ans = min(ans ,depth)
            if node:
                queue.append((node.left,depth+1))
                queue.append((node.right,depth+1))
        return ans
